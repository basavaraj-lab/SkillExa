def test_sandboxed_python_code_execution(client):
    code = 'print("Hello from SkillExa Sandbox")'
    res = client.post(
        "/api/coding/execute",
        json={"language": "python", "code": code},
    )
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["status"] == "PASSED"
    assert "Hello from SkillExa Sandbox" in data["stdout"]
    assert data["runtime_ms"] >= 0.0


def test_sandboxed_execution_syntax_error(client):
    code = 'def broken_func(\n  # invalid syntax'
    res = client.post(
        "/api/coding/execute",
        json={"language": "python", "code": code},
    )
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["status"] == "RUNTIME_ERROR"
    assert "SyntaxError" in data["stderr"]
