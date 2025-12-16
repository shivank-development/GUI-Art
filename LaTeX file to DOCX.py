import pypandoc

clcoding = "clcoding.tex"
out = "clcoding_11.docx"

pypandoc.convert_file(
    clcoding,
    to="docx",
    outputfile=out,
    extra_args=["--standalone"]
)

print("Saved:", out)
