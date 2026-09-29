import subprocess
import sys

MODEL_PATH = "inclusionAI/LLaDA2.0-mini"
HOST = "0.0.0.0"
PORT = "30000"

command = [
    sys.executable,
    "-m",
    "sglang.launch_server",
    "--model-path",
    MODEL_PATH,
    "--host",
    HOST,
    "--port",
    PORT,
    "--trust-remote-code",
    "--dtype",
    "half",
    "--attention-backend",
    "triton",
]

print("=" * 60)
print("Starting LLaDA2.0-mini with SGLang")
print(f"Model  : {MODEL_PATH}")
print(f"Server : http://localhost:{PORT}")
print("=" * 60)

try:
    subprocess.run(command, check=True)
except KeyboardInterrupt:
    print("\nStopping SGLang server...")
except subprocess.CalledProcessError as error:
    print(f"SGLang server exited with error: {error}")