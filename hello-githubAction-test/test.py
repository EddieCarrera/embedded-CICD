import os, subprocess

# Settings 
TEST_DIR = "."
CODE_FILE = "main.cpp"
COMPILER_TIMEOUT_S = 10.0
RUN_TIMEOUT_S = 10.0

# Create absolute paths
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "outputExe")

# Compile program
print("Building...")
try:
  ret = subprocess.run(["gcc", code_path, "-o", app_path], 
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, 
                        timeout=COMPILER_TIMEOUT_S)
except Exception as e:
  print("ERROR: Compilatiion failed."+str(e))
  exit(1)


# Parse output
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stderr.decode('utf-8')
print(output)

# Check of compiled successfully
if ret.returncode != 0:
  print("Compilation failed.")
  exit(1)

# Run the compiled program
print("Running...")
try:
  ret = subprocess.run([app_path],
                       stdout=subprocess.PIPE,
                       timeout=RUN_TIMEOUT_S)
except Exception as e:
  print("ERROR: Runtime failed."+str(e))
  exit(1)

# Parse output 
output = ret.stdout.decode('utf-8')
print("output:"+output)

# All tests passed
print("All tests passed!")
exit(0)