#!/bin/bash
# test_generate_pdf.sh

# Exit on any error
set -e

# Track if the test passes
TEST_PASSED=false

# Setup mock pandoc
mkdir -p test_mock_bin
cat << 'MOCK' > test_mock_bin/pandoc
#!/bin/bash
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -o) output_file="$2"; shift ;;
    esac
    shift
done
if [ -n "$output_file" ]; then
    touch "$output_file"
fi
MOCK
chmod +x test_mock_bin/pandoc

export PATH="$(pwd)/test_mock_bin:$PATH"

# Setup dummy input files
mkdir -p riemann_hypothesis/inprogress/
touch riemann_hypothesis/inprogress/01-fibration_motivique_fr.md
touch riemann_hypothesis/inprogress/01-fibration_motivique_en.md

# Make sure outputs don't exist before running
rm -f "riemann_hypothesis/preuve_fibration_motivique_01_fr.pdf"
rm -f "riemann_hypothesis/preuve_fibration_motivique_01_en.pdf"

# Run the script
./generate_pdf.sh > /dev/null

# Verify outputs
if [ -f "riemann_hypothesis/preuve_fibration_motivique_01_fr.pdf" ] && [ -f "riemann_hypothesis/preuve_fibration_motivique_01_en.pdf" ]; then
    echo "Test passed: PDF files generated."
    TEST_PASSED=true
else
    echo "Test failed: PDF files not generated."
fi

# Cleanup
rm -rf test_mock_bin
rm -f "riemann_hypothesis/preuve_fibration_motivique_01_fr.pdf"
rm -f "riemann_hypothesis/preuve_fibration_motivique_01_en.pdf"

# Exit with appropriate status
if [ "$TEST_PASSED" = true ]; then
    exit 0
else
    exit 1
fi
