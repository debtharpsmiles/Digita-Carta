# Zero-dollar Sovereign: local GitHub Actions experiment

**No OpenAI API key, Hugging Face paid inference, subscription, or card is needed.**

GitHub currently offers free standard hosted runners for public repositories. The experimental workflow downloads the Apache-2.0 licensed [Qwen3 1.7B quantized model](https://huggingface.co/ggml-org/Qwen3-1.7B-GGUF), verifies its published SHA256, compiles [llama.cpp](https://github.com/ggml-org/llama.cpp), and runs inference entirely inside the temporary GitHub runner.

This is not the GPT-6 assistant from the original conversation. A small local model may give weaker answers or fail to compose useful ones. The workflow refuses some suspicious output patterns and labels all public contributions clearly.

## How to try it

1. Merge this proposed branch into the public `Digita-Carta` repository.
2. In GitHub, select **Actions** → **Sovereign - zero-cost local reasoning experiment** → **Run workflow**.
3. Leave **preview** selected. A GitHub runner will attempt to build and run the model; read the workflow logs. Preview does **not** publish to Discussions.
4. If the build and preview succeed and the output is thoughtful, run again with **publish** selected. That creates at most one AI-labeled comment in Discussion #1. Repeating the command without a new human comment produces nothing.

The first run may be slow because a 1.28 GB model must be downloaded and `llama.cpp` compiled. Public GitHub Actions still have operational limits and acceptable-use policies; this setup does not require billable premium runners. There is no automatic schedule yet, so this is an experimental public-participation pathway, not an independently scheduled production bot.

**Important:** Do not set the `OPENAI_API_KEY` secret for this method. The separate [paid API runner](../.github/workflows/sovereign-discussion.yml) remains inactive without that secret. Do not select or enable larger billable GitHub runners.

## After first successful preview

A proposed next stage is adding a conservative schedule, checking for new human comments *before* downloading the model, and enforcing a daily posting limit. Do not enable unattended public posting until the model's actual output quality and the workflow build have been verified.
