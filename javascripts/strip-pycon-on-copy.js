document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("button.md-clipboard.md-icon").forEach((button) => {
        button.addEventListener("click", (event) => {
            const codeBlock = button.closest("pre").querySelector("code");
            if (!codeBlock) return;

            const lines = codeBlock.innerText.split("\n");
            const cleaned = lines
                .filter(line => /^>>> |^\.\.\. /.test(line))
                .map(line =>
                    line.replace(/^>>> |^\.\.\. /, '')
                        .replace(/\s*#\s*doctest:\s*\+SKIP/, '')
                        .replace(/\s*#\s*doctest:\s*\+ELLIPSIS/, '')
                        .replace(/\s*#\s*doctest:\s*\+IGNORE_EXCEPTION_DETAIL/, '')
                )
                .join("\n");

            navigator.clipboard.writeText(cleaned);
        });
    });
});
