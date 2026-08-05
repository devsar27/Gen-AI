# AI Operations Assistant

## Project overview

The AI Operations Assistant is a CLI-based tool for IT operations troubleshooting and documentation lookup.
It is designed to help operations engineers, SREs, and IT support professionals answer infrastructure questions, explain operational concepts, and retrieve documentation-style best practices.

## Scope

Primary focus:
- IT operations knowledge lookup
- documentation-style explanations
- infrastructure troubleshooting guidance
- short, actionable recommendations

Search tool:
- Google search via `GoogleSerperAPIWrapper`

## Architecture

- `cli.py` — command-line interface and interaction loop
- `agent_core.py` — constructs the LangChain agent and configures tool behavior
- `tools.py` — defines external tool wrappers, starting with search
- `prompts.py` — contains system prompts and prompt templates
- `config.py` — loads environment settings and API keys
- `utils.py` — formatting helpers and reusable utilities

## User stories

- As an operations engineer, I can ask the assistant questions about Linux, Kubernetes, networking, and monitoring.
- As an IT support specialist, I can request documentation-style explanations and receive concise, accurate answers.
- As an analyst, I can ask for troubleshooting steps and receive structured guidance.

## Sample CLI flow

```
$ python apps/ai_ops_assistant/cli.py
Welcome to AI Ops Assistant.
Ask an operations question or type `exit`.

> What does Kubernetes CrashLoopBackOff mean?

AI: CrashLoopBackOff means a container is repeatedly failing to start. Check the pod logs, validate the startup command, and verify readiness dependencies. Search the web for recent Kubernetes docs if needed.
```

## Milestone plan

1. Design & CLI scaffold
   - create the project layout and prompt design
   - implement a CLI loop with placeholders
2. Add search tool
   - integrate `GoogleSerperAPIWrapper`
   - let the agent call the tool for documentation lookup
3. Add operations context and state
   - improve prompt guidance
   - optionally add a local ops knowledge layer
4. Polish output and documentation
   - make the assistant resume-ready
