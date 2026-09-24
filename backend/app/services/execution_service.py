import os
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Optional, Tuple
from backend.app.config import settings
from backend.app.models.coding import SubmissionStatusEnum
from backend.app.schemas.coding import ExecutionResultResponse


class SandboxedExecutionService:
    @staticmethod
    def _get_isolated_env() -> dict:
        """Create sanitized environment variables without database or secret credentials."""
        safe_keys = ["PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP", "LOCALAPPDATA", "PROGRAMFILES"]
        clean_env = {k: os.environ[k] for k in safe_keys if k in os.environ}
        # Explicitly ensure no sensitive variables are forwarded
        clean_env["PYTHONUNBUFFERED"] = "1"
        clean_env["PYTHONDONTWRITEBYTECODE"] = "1"
        return clean_env

    @staticmethod
    def execute_code(
        language: str,
        code: str,
        custom_input: Optional[str] = None,
        timeout_seconds: Optional[int] = None,
    ) -> ExecutionResultResponse:
        lang = language.lower().strip()
        timeout = timeout_seconds or settings.SANDBOX_EXECUTION_TIMEOUT_SECONDS
        isolated_dir = tempfile.mkdtemp(prefix="skillexa_sandbox_")
        env = SandboxedExecutionService._get_isolated_env()

        start_time = time.time()
        compile_output = None
        stdout = ""
        stderr = ""
        status = SubmissionStatusEnum.PASSED
        error_message = None

        try:
            # 1. PYTHON
            if lang in ["python", "py", "python3"]:
                file_path = os.path.join(isolated_dir, "solution.py")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(code)

                # Use Python executable from current venv or system
                py_exec = sys.executable
                cmd = [py_exec, file_path]

                res = subprocess.run(
                    cmd,
                    input=custom_input or "",
                    text=True,
                    capture_output=True,
                    cwd=isolated_dir,
                    env=env,
                    timeout=timeout,
                )
                stdout = res.stdout
                stderr = res.stderr
                if res.returncode != 0:
                    status = SubmissionStatusEnum.RUNTIME_ERROR
                    error_message = stderr

            # 2. JAVASCRIPT / NODE.JS
            elif lang in ["javascript", "js", "node"]:
                file_path = os.path.join(isolated_dir, "solution.js")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(code)

                cmd = ["node", file_path]
                res = subprocess.run(
                    cmd,
                    input=custom_input or "",
                    text=True,
                    capture_output=True,
                    cwd=isolated_dir,
                    env=env,
                    timeout=timeout,
                )
                stdout = res.stdout
                stderr = res.stderr
                if res.returncode != 0:
                    status = SubmissionStatusEnum.RUNTIME_ERROR
                    error_message = stderr

            # 3. C (GCC / Clang)
            elif lang in ["c", "clang"]:
                src_path = os.path.join(isolated_dir, "solution.c")
                exe_name = "solution.exe" if os.name == "nt" else "./solution"
                exe_path = os.path.join(isolated_dir, exe_name)

                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(code)

                # Compilation step
                compile_res = subprocess.run(
                    ["gcc", src_path, "-O2", "-o", exe_path],
                    text=True,
                    capture_output=True,
                    cwd=isolated_dir,
                    env=env,
                    timeout=timeout,
                )
                if compile_res.returncode != 0:
                    status = SubmissionStatusEnum.COMPILATION_ERROR
                    compile_output = compile_res.stderr
                    error_message = compile_res.stderr
                else:
                    # Run executable
                    run_res = subprocess.run(
                        [exe_path],
                        input=custom_input or "",
                        text=True,
                        capture_output=True,
                        cwd=isolated_dir,
                        env=env,
                        timeout=timeout,
                    )
                    stdout = run_res.stdout
                    stderr = run_res.stderr
                    if run_res.returncode != 0:
                        status = SubmissionStatusEnum.RUNTIME_ERROR
                        error_message = stderr

            # 4. C++ (G++)
            elif lang in ["cpp", "c++", "cplusplus"]:
                src_path = os.path.join(isolated_dir, "solution.cpp")
                exe_name = "solution.exe" if os.name == "nt" else "./solution"
                exe_path = os.path.join(isolated_dir, exe_name)

                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(code)

                compile_res = subprocess.run(
                    ["g++", "-std=c++17", src_path, "-O2", "-o", exe_path],
                    text=True,
                    capture_output=True,
                    cwd=isolated_dir,
                    env=env,
                    timeout=timeout,
                )
                if compile_res.returncode != 0:
                    status = SubmissionStatusEnum.COMPILATION_ERROR
                    compile_output = compile_res.stderr
                    error_message = compile_res.stderr
                else:
                    run_res = subprocess.run(
                        [exe_path],
                        input=custom_input or "",
                        text=True,
                        capture_output=True,
                        cwd=isolated_dir,
                        env=env,
                        timeout=timeout,
                    )
                    stdout = run_res.stdout
                    stderr = run_res.stderr
                    if run_res.returncode != 0:
                        status = SubmissionStatusEnum.RUNTIME_ERROR
                        error_message = stderr

            # 5. JAVA
            elif lang in ["java"]:
                src_path = os.path.join(isolated_dir, "Main.java")
                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(code)

                compile_res = subprocess.run(
                    ["javac", src_path],
                    text=True,
                    capture_output=True,
                    cwd=isolated_dir,
                    env=env,
                    timeout=timeout,
                )
                if compile_res.returncode != 0:
                    status = SubmissionStatusEnum.COMPILATION_ERROR
                    compile_output = compile_res.stderr
                    error_message = compile_res.stderr
                else:
                    run_res = subprocess.run(
                        ["java", "Main"],
                        input=custom_input or "",
                        text=True,
                        capture_output=True,
                        cwd=isolated_dir,
                        env=env,
                        timeout=timeout,
                    )
                    stdout = run_res.stdout
                    stderr = run_res.stderr
                    if run_res.returncode != 0:
                        status = SubmissionStatusEnum.RUNTIME_ERROR
                        error_message = stderr

            else:
                status = SubmissionStatusEnum.INTERNAL_ERROR
                error_message = f"Language '{language}' execution sandbox is not supported."

        except subprocess.TimeoutExpired:
            status = SubmissionStatusEnum.TIMEOUT
            error_message = f"Time Limit Exceeded (CPU execution timed out after {timeout} seconds)."
        except FileNotFoundError as fnf:
            # Compiler/interpreter binary not found on local host; simulate or return descriptive runtime error
            status = SubmissionStatusEnum.INTERNAL_ERROR
            error_message = f"Compiler/runtime for {language} is not installed on the server environment ({fnf})."
        except Exception as e:
            status = SubmissionStatusEnum.RUNTIME_ERROR
            error_message = f"Sandbox execution error: {str(e)}"
        finally:
            # 6. Automatic Clean-up of Isolated Scratch Directory
            shutil.rmtree(isolated_dir, ignore_errors=True)

        elapsed_ms = round((time.time() - start_time) * 1000.0, 2)
        memory_kb = 4096.0  # Estimated sandbox baseline

        return ExecutionResultResponse(
            status=status,
            stdout=stdout.strip(),
            stderr=stderr.strip(),
            compile_output=compile_output,
            runtime_ms=elapsed_ms,
            memory_kb=memory_kb,
            error_message=error_message,
        )

    @staticmethod
    def run_test_cases(
        language: str,
        code: str,
        test_cases: list,
    ) -> Tuple[SubmissionStatusEnum, int, int, str]:
        """
        Execute code across problem test cases.
        Returns: (status, test_cases_passed, total_test_cases, output_logs)
        """
        passed_count = 0
        total_count = len(test_cases)
        logs = []

        if total_count == 0:
            return SubmissionStatusEnum.PASSED, 0, 0, "No test cases configured."

        for idx, tc in enumerate(test_cases):
            tc_input = tc.get("input", "")
            tc_expected = tc.get("expected", "").strip()

            res = SandboxedExecutionService.execute_code(
                language=language,
                code=code,
                custom_input=tc_input,
                timeout_seconds=settings.SANDBOX_EXECUTION_TIMEOUT_SECONDS,
            )

            if res.status != SubmissionStatusEnum.PASSED:
                logs.append(f"Test #{idx+1}: {res.status.value} - {res.error_message}")
                return res.status, passed_count, total_count, "\n".join(logs)

            actual_out = res.stdout.strip()
            if actual_out == tc_expected:
                passed_count += 1
                logs.append(f"Test #{idx+1}: PASSED ({res.runtime_ms}ms)")
            else:
                logs.append(f"Test #{idx+1}: FAILED\nInput: {tc_input}\nExpected: {tc_expected}\nActual: {actual_out}")
                return SubmissionStatusEnum.FAILED, passed_count, total_count, "\n".join(logs)

        return SubmissionStatusEnum.PASSED, passed_count, total_count, "\n".join(logs)
