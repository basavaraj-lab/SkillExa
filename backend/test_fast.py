import sys, os
sys.path.insert(0, os.path.abspath('.'))
import subprocess, tempfile, shutil, time
from backend.app.models.coding import SubmissionStatusEnum

def fast_run_test_cases(language: str, code: str, test_cases: list):
    lang = language.lower().strip()
    isolated_dir = tempfile.mkdtemp(prefix="skillexa_fast_")
    compile_timeout = 15
    run_timeout = 5
    logs = []
    passed_count = 0
    total_count = len(test_cases)
    
    clean_env = {k: os.environ[k] for k in ["PATH", "SYSTEMROOT", "WINDIR", "TEMP", "TMP"] if k in os.environ}
    clean_env["PYTHONUNBUFFERED"] = "1"

    try:
        # Prepare & Compile
        if lang in ["python", "py", "python3"]:
            src_path = os.path.join(isolated_dir, "solution.py")
            with open(src_path, "w", encoding="utf-8") as f:
                f.write(code)
            run_cmd = [sys.executable, src_path]
            
        elif lang in ["c", "clang"]:
            src_path = os.path.join(isolated_dir, "solution.c")
            exe_path = os.path.join(isolated_dir, "solution.exe")
            with open(src_path, "w", encoding="utf-8") as f:
                f.write(code)
            c_res = subprocess.run(["gcc", src_path, "-O2", "-o", exe_path], capture_output=True, text=True, cwd=isolated_dir, env=clean_env, timeout=compile_timeout)
            if c_res.returncode != 0:
                return SubmissionStatusEnum.COMPILATION_ERROR, 0, total_count, c_res.stderr
            run_cmd = [exe_path]

        elif lang in ["cpp", "c++", "cplusplus"]:
            src_path = os.path.join(isolated_dir, "solution.cpp")
            exe_path = os.path.join(isolated_dir, "solution.exe")
            with open(src_path, "w", encoding="utf-8") as f:
                f.write(code)
            c_res = subprocess.run(["g++", "-std=c++17", src_path, "-O2", "-o", exe_path], capture_output=True, text=True, cwd=isolated_dir, env=clean_env, timeout=compile_timeout)
            if c_res.returncode != 0:
                return SubmissionStatusEnum.COMPILATION_ERROR, 0, total_count, c_res.stderr
            run_cmd = [exe_path]

        elif lang in ["java"]:
            src_path = os.path.join(isolated_dir, "Main.java")
            with open(src_path, "w", encoding="utf-8") as f:
                f.write(code)
            c_res = subprocess.run(["javac", src_path], capture_output=True, text=True, cwd=isolated_dir, env=clean_env, timeout=compile_timeout)
            if c_res.returncode != 0:
                return SubmissionStatusEnum.COMPILATION_ERROR, 0, total_count, c_res.stderr
            run_cmd = ["java", "Main"]
        else:
            return SubmissionStatusEnum.INTERNAL_ERROR, 0, total_count, f"Unsupported language: {lang}"

        # Run test cases
        for idx, tc in enumerate(test_cases):
            tc_input = tc.get("input", "")
            tc_expected = tc.get("expected", "").strip()
            
            t0 = time.time()
            r_res = subprocess.run(run_cmd, input=tc_input, text=True, capture_output=True, cwd=isolated_dir, env=clean_env, timeout=run_timeout)
            dur_ms = round((time.time() - t0) * 1000, 1)

            if r_res.returncode != 0:
                logs.append(f"Test #{idx+1}: RUNTIME_ERROR - {r_res.stderr}")
                return SubmissionStatusEnum.RUNTIME_ERROR, passed_count, total_count, "\n".join(logs)

            actual = r_res.stdout.strip()
            if actual == tc_expected:
                passed_count += 1
                logs.append(f"Test #{idx+1}: PASSED ({dur_ms}ms)")
            else:
                logs.append(f"Test #{idx+1}: FAILED\nInput: {tc_input}\nExpected: {tc_expected}\nActual: {actual}")
                return SubmissionStatusEnum.FAILED, passed_count, total_count, "\n".join(logs)

        return SubmissionStatusEnum.PASSED, passed_count, total_count, "\n".join(logs)

    except subprocess.TimeoutExpired:
        return SubmissionStatusEnum.TIMEOUT, passed_count, total_count, "Execution timed out."
    except Exception as e:
        return SubmissionStatusEnum.RUNTIME_ERROR, passed_count, total_count, str(e)
    finally:
        shutil.rmtree(isolated_dir, ignore_errors=True)

if __name__ == "__main__":
    from test_execution import c_code, cpp_code, java_code, python_code, test_cases
    for lang, code in [("c", c_code), ("cpp", cpp_code), ("java", java_code), ("python", python_code)]:
        st = time.time()
        status, passed, total, logs = fast_run_test_cases(lang, code, test_cases)
        dur = round(time.time() - st, 2)
        print(f"[{lang}] Result: {status.value} ({passed}/{total}) in {dur}s")
        if status.value != "PASSED":
            print(logs)

