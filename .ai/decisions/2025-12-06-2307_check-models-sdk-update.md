# Decision Record: Update check_models.py to New Google GenAI SDK

**Previous Record Hash:** `db9a8209be95773502c5bde5f5be659215c4a46bf2b1efb5974a8666d73dac35`

## Context
User reported that `src/check_models.py` had broken dependencies. The script was using the old `google.generativeai` SDK while the rest of the project (specifically `engine.py`) had migrated to the newer `google.genai` SDK.

## Decision
Updated `check_models.py` to use the same SDK pattern as `engine.py`:
- Changed import from `google.generativeai as genai` to `from google import genai`
- Changed configuration from `genai.configure()` to client-based `genai.Client()`
- Changed model listing from `genai.list_models()` to `client.models.list()`
- Updated attribute access from `supported_generation_methods` to `supported_actions`

The new SDK uses a different Model schema where the generation capabilities are exposed via `supported_actions` instead of `supported_generation_methods`.

## Changes
- `src/check_models.py`: Migrated to new `google.genai` SDK client pattern

## Verification
```
$ python src/check_models.py
Available Models:
models/gemini-2.5-flash
models/gemini-2.5-pro
models/gemini-2.0-flash-exp
models/gemini-2.0-flash
...
```
Script executes successfully and lists all models supporting `generateContent`.
