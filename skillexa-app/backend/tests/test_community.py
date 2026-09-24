def test_community_public_discovery_and_filtering(client, faculty_token, student_token):
    # 1. Faculty creates Community Note (visibility = community)
    client.post(
        "/api/faculty/notes",
        headers={"Authorization": f"Bearer {faculty_token}"},
        json={
            "title": "Community AVL Tree Rotations & Balancing",
            "content": "AVL trees are self-balancing binary search trees...",
            "section": "dsa",
            "subject": "DSA in Python",
            "topic": "Trees",
            "visibility": "community",
            "published": True,
        },
    )

    # 2. Student from another college queries community feed
    comm_res = client.get(
        "/api/community/content?category=dsa&subject=Python&topic=Trees",
        headers={"Authorization": f"Bearer {student_token}"},
    )
    assert comm_res.status_code == 200
    items = comm_res.json()["data"]["items"]
    assert len(items) >= 1
    assert "AVL Tree" in items[0]["title"]
    assert items[0]["is_verified_faculty"] is True
