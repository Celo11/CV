import sys
import subprocess
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent
    scripts = sorted(root.glob("make_*.py"))
    
    print(f"Found {len(scripts)} generation script(s).\n")
    success = 0
    failed = []
    
    for script in scripts:
        print(f"Generating from {script.name}...", end=" ", flush=True)
        res = subprocess.run([sys.executable, str(script)], cwd=str(root), capture_output=True, text=True)
        if res.returncode == 0:
            print("OK")
            success += 1
        else:
            print("FAILED")
            if res.stderr:
                print(res.stderr.strip())
            failed.append(script.name)
            
    print(f"\nCompleted: {success}/{len(scripts)} generated successfully.")
    if failed:
        print(f"Failed scripts: {', '.join(failed)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
