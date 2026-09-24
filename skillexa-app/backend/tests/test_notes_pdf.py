import io


def test_faculty_notes_crud_and_publishing(client, faculty_token, student_token):
    # 1. Create Faculty Note
    create_res = client.post(
        "/api/faculty/notes",
        headers={"Authorization": f"Bearer {faculty_token}"},
        json={
            "title": "Embedded Systems GPIO Registers",
            "content": "GPIO pins operate in Push-Pull or Open-Drain configurations...",
            "section": "engineering",
            "subject": "Embedded Systems",
            "topic": "Microcontrollers",
            "important_concepts": ["MODER sets pin mode", "PUPDR controls internal pull-ups"],
            "quick_revision": "Configure MODER before accessing IDR/ODR registers.",
            "visibility": "college",
            "published": True,
        },
    )
    assert create_res.status_code == 201
    note_id = create_res.json()["data"]["id"]

    # 2. Student views topic notes
    student_notes_res = client.get(
        "/api/notes?subject=Embedded&topic=Microcontrollers",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert student_notes_res.status_code == 200
    assert len(student_notes_res.json()["data"]) >= 1

    # 3. Unpublish note
    unpub_res = client.post(
        f"/api/faculty/notes/{note_id}/unpublish",
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert unpub_res.status_code == 200
    assert unpub_res.json()["data"]["published"] is False


def test_pdf_upload_and_version_replacement(client, faculty_token):
    # 1. Upload initial PDF
    pdf_content = b"%PDF-1.4 sample PDF content test"
    upload_res = client.post(
        "/api/faculty/pdf-notes",
        headers={"Authorization": f"Bearer {faculty_token}"},
        data={
            "title": "Microcontrollers Hardware Guide",
            "subject": "Embedded Systems",
            "topic": "Microcontrollers",
            "visibility": "college",
        },
        files={"file": ("guide.pdf", io.BytesIO(pdf_content), "application/pdf")},
    )
    assert upload_res.status_code == 201
    pdf_data = upload_res.json()["data"]
    pdf_id = pdf_data["id"]
    assert pdf_data["version"] == 1

    # 2. Replace PDF with updated edition
    new_pdf_content = b"%PDF-1.4 updated v2 PDF content"
    replace_res = client.put(
        f"/api/faculty/pdf-notes/{pdf_id}/replace",
        headers={"Authorization": f"Bearer {faculty_token}"},
        files={"file": ("guide_v2.pdf", io.BytesIO(new_pdf_content), "application/pdf")},
    )
    assert replace_res.status_code == 200
    replaced_data = replace_res.json()["data"]
    assert replaced_data["id"] == pdf_id
    assert replaced_data["version"] == 2
