def update_version():
    try:
        with open('.git/COMMIT_EDITMSG', 'r') as commit_file:
            commit_lines = commit_file.readlines()

        stripped_lines = [line.lstrip('# ').rstrip() + '\n' if line.startswith('#') else line for line in commit_lines]

        with open('version', 'a') as version_file:
            version_file.write(''.join(stripped_lines))

    except FileNotFoundError:
        print(".git/COMMIT_EDITMSG file not found.")
    except Exception as e:
        print("An error occurred:", e)

update_version()
