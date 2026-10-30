with open("backend/app/services/execution_service.py", "r", encoding="utf-8") as f:
    text = f.read()

new_run_test_cases = '''    @staticmethod
    def run_test_cases(
        language: str,
        code: str,
        test_cases: list,
    ) -> Tuple[SubmissionStatusEnum, int, int, str]:
        """
        Execute code across problem test cases with single-compilation optimization.
        Returns: (status, test_cases_passed, total_test_cases, output_logs)
        """
        lang = language.lower().strip()
        passed_count = 0
        total_count = len(test_cases)
        logs = []

        if total_count == 0:
            return SubmissionStatusEnum.PASSED, 0, 0, "No test cases configured."

        isolated_dir = tempfile.mkdtemp(prefix="skillexa_runner_")
        env = SandboxedExecutionService._get_isolated_env()
        compile_timeout = 15
        run_timeout = settings.SANDBOX_EXECUTION_TIMEOUT_SECONDS or 5

        try:
            # 1. Compile or Prepare executable
            if lang in ["python", "py", "python3"]:
                src_path = os.path.join(isolated_dir, "solution.py")
                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(code)
                run_cmd = [sys.executable, src_path]

            elif lang in ["c", "clang"]:
                src_path = os.path.join(isolated_dir, "solution.c")
                exe_name = "solution.exe" if os.name == "nt" else "./solution"
                exe_path = os.path.join(isolated_dir, exe_name)
                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(code)
                c_res = subprocess.run(["gcc", src_path, "-O2", "-o", exe_path], capture_output=True, text=True, cwd=isolated_dir, env=env, timeout=compile_timeout)
                if c_res.returncode != 0:
                    return SubmissionStatusEnum.COMPILATION_ERROR, 0, total_count, c_res.stderr or "GCC Compilation Failed"
                run_cmd = [exe_path]

            elif lang in ["cpp", "c++", "cplusplus"]:
                src_path = os.path.join(isolated_dir, "solution.cpp")
                exe_name = "solution.exe" if os.name == "nt" else "./solution"
                exe_path = os.path.join(isolated_dir, exe_name)
                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(code)
                c_res = subprocess.run(["g++", "-std=c++17", src_path, "-O2", "-o", exe_path], capture_output=True, text=True, cwd=isolated_dir, env=env, timeout=compile_timeout)
                if c_res.returncode != 0:
                    return SubmissionStatusEnum.COMPILATION_ERROR, 0, total_count, c_res.stderr or "G++ Compilation Failed"
                run_cmd = [exe_path]

            elif lang in ["java"]:
                src_path = os.path.join(isolated_dir, "Main.java")
                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(code)
                try:
                    c_res = subprocess.run(["javac", src_path], capture_output=True, text=True, cwd=isolated_dir, env=env, timeout=compile_timeout)
                    if c_res.returncode != 0:
                        return SubmissionStatusEnum.COMPILATION_ERROR, 0, total_count, c_res.stderr or "Java compiler error"
                    run_cmd = ["java", "Main"]
                except Exception as je:
                    return SubmissionStatusEnum.INTERNAL_ERROR, 0, total_count, f"Java runtime environment error: {str(je)}"

            elif lang in ["javascript", "js", "node"]:
                src_path = os.path.join(isolated_dir, "solution.js")
                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(code)
                run_cmd = ["node", src_path]
            else:
                return SubmissionStatusEnum.INTERNAL_ERROR, 0, total_count, f"Language '{language}' execution sandbox is not supported."

            # 2. Run compiled command for each test case
            for idx, tc in enumerate(test_cases):
                tc_input = tc.get("input", "")
                tc_expected = tc.get("expected", "").strip()

                t0 = time.time()
                r_res = subprocess.run(
                    run_cmd,
                    input=tc_input or "",
                    text=True,
                    capture_output=True,
                    cwd=isolated_dir,
                    env=env,
                    timeout=run_timeout,
                )
                dur_ms = round((time.time() - t0) * 1000.0, 1)

                if r_res.returncode != 0:
                    logs.append(f"Test #{idx+1}: RUNTIME_ERROR - {r_res.stderr}")
                    return SubmissionStatusEnum.RUNTIME_ERROR, passed_count, total_count, "\\n".join(logs)

                actual = r_res.stdout.strip()
                if actual == tc_expected:
                    passed_count += 1
                    logs.append(f"Test #{idx+1}: PASSED ({dur_ms}ms)")
                else:
                    logs.append(f"Test #{idx+1}: FAILED\\nInput: {tc_input}\\nExpected: {tc_expected}\\nActual: {actual}")
                    return SubmissionStatusEnum.FAILED, passed_count, total_count, "\\n".join(logs)

            return SubmissionStatusEnum.PASSED, passed_count, total_count, "\\n".join(logs)

        except subprocess.TimeoutExpired:
            return SubmissionStatusEnum.TIMEOUT, passed_count, total_count, f"Time Limit Exceeded (CPU execution timed out after {run_timeout} seconds)."
        except FileNotFoundError as fnf:
            return SubmissionStatusEnum.INTERNAL_ERROR, passed_count, total_count, f"Compiler/runtime for {language} is not installed on the server environment ({fnf})."
        except Exception as e:
            return SubmissionStatusEnum.RUNTIME_ERROR, passed_count, total_count, f"Sandbox execution error: {str(e)}"
        finally:
            shutil.rmtree(isolated_dir, ignore_errors=True)
'''

# Find def run_test_cases
start_idx = text.find("    @staticmethod\n    def run_test_cases(")
if start_idx != -1:
    text = text[:start_idx] + new_run_test_cases

with open("backend/app/services/execution_service.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated execution_service.py successfully!")

