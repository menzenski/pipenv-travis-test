import subprocess


def test_using_subprocess_check(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    subprocess.check_call([
        'cd',
        tmpdir.strpath,
        ])
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1
