#!/usr/bin/env python3
import subprocess
import sys
import tempfile
import os

# Predefined commit types and scopes
TYPES = ["feature", "fix", "new coverage", "refactor", "docs"]
SCOPES = ["hotfix", "regression", "new feature", "core"]

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"❌ Error running command: {cmd}\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def get_staged_files():
    files = run_cmd("git diff --cached --name-only")
    return files.splitlines()

def prompt_choice(prompt, options):
    print(prompt)
    for i, opt in enumerate(options, start=1):
        print(f"  {i}. {opt}")
    choice = input("Select number or type custom: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(options):
        return options[int(choice)-1]
    return choice  # custom input

def edit_message(message):
    # Open temp file with current message
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".tmp") as tf:
        tf.write(message)
        tf.flush()
        editor = os.environ.get("EDITOR", "vi")  # default to nano if $EDITOR not set
        subprocess.run([editor, tf.name])
        tf.seek(0)
        edited_message = open(tf.name).read().strip()
    os.unlink(tf.name)
    return edited_message

def main():
    staged_files = get_staged_files()
    if not staged_files:
        print("⚠️ No staged files found. Please 'git add' your changes first.")
        sys.exit(0)

    print("\n📄 Staged files:")
    for f in staged_files:
        print(f"  - {f}")

    # Required inputs
    ticket = input("\nEnter ticket number (e.g. QA-1234): ").strip()
    if not ticket:
        print("❌ Ticket number is required.")
        sys.exit(1)

    description = input("Enter short description of the changes: ").strip()
    reason = input("Enter reason for the change: ").strip()
    owner = input("Enter owner name: ").strip()

    # Type & scope selection
    commit_type = prompt_choice("Select commit type:", TYPES)
    scope = prompt_choice("Select scope:", SCOPES)
    type_line = f"{commit_type}({scope})"

    # Build initial commit message
    full_message = f"{ticket} : {description}\n\nReason for change : {reason}\nType : {type_line}\nOwner : {owner}"

    # Preview
    print("\n✅ Commit Message Preview:\n" + "-"*50)
    print(full_message)
    print("-"*50)

    # Option to edit
    edit_choice = input("Do you want to edit the commit message? [y/N]: ").strip().lower()
    if edit_choice == "y":
        full_message = edit_message(full_message)
        print("\n✏️  Edited Commit Message:\n" + "-"*50)
        print(full_message)
        print("-"*50)

    confirm = input("Proceed with commit? [Y/n]: ").strip().lower()
    if confirm == "n":
        print("🚫 Commit cancelled.")
        sys.exit(0)

    # Commit
    subprocess.run(['git', 'commit', '-m', full_message])
    print("🎉 Commit created successfully!")

if __name__ == "__main__":
    main()
