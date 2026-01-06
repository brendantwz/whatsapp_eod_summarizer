# Workflow Diagram - WhatsApp EOD Report Generator

## 🔄 Complete Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                         INPUT PHASE                              │
└─────────────────────────────────────────────────────────────────┘
                              ▼
                    ┌─────────────────┐
                    │  WhatsApp Chat  │
                    │   Export .txt   │
                    │                 │
                    │ ✓ Timestamps    │
                    │ ✓ Senders       │
                    │ ✓ Messages      │
                    │ ✗ System msgs   │
                    │ ✗ Unicode junk  │
                    └─────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       PARSING PHASE                              │
│                     (parser.py / run.py)                         │
└─────────────────────────────────────────────────────────────────┘
                              ▼
                    ┌─────────────────┐
                    │  Regex Pattern  │
                    │    Matching     │
                    └─────────────────┘
                              ▼
              ┌──────────────┴──────────────┐
              ▼                             ▼
    ┌─────────────────┐         ┌─────────────────┐
    │  Valid Message  │         │ System Message  │
    │  (Keep & Clean) │         │  (Filter Out)   │
    └─────────────────┘         └─────────────────┘
              ▼                             ▼
    ┌─────────────────┐              [Discarded]
    │ Clean Unicode   │
    │ Remove \u2068   │
    └─────────────────┘
              ▼
    ┌─────────────────┐
    │ Multi-line      │
    │ Concatenation   │
    └─────────────────┘
              ▼
    ┌─────────────────┐
    │  JSON Output    │
    │  [{timestamp,   │
    │    sender,      │
    │    message}]    │
    └─────────────────┘
              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     VALIDATION PHASE                             │
│                  (First 10 messages preview)                     │
└─────────────────────────────────────────────────────────────────┘
              ▼
    ┌─────────────────┐
    │  Quality Check  │
    │  ✓ Timestamps?  │
    │  ✓ Clean text?  │
    │  ✓ No garbage?  │
    └─────────────────┘
              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    SUMMARIZATION PHASE                           │
│                (summarizer.py + AI Provider)                     │
└─────────────────────────────────────────────────────────────────┘
              ▼
    ┌─────────────────┐
    │  Format for AI  │
    │  [timestamp]    │
    │  Sender: Msg    │
    └─────────────────┘
              ▼
    ┌─────────────────┐
    │  Create Prompt  │
    │  + Rules        │
    │  + Structure    │
    │  + Context      │
    └─────────────────┘
              ▼
        ┌──────┴──────┐
        ▼             ▼
┌──────────────┐  ┌──────────────┐
│   Claude     │  │   GPT-4      │
│ (Anthropic)  │  │  (OpenAI)    │
└──────────────┘  └──────────────┘
        │             │
        └──────┬──────┘
               ▼
    ┌─────────────────┐
    │   AI Analysis   │
    │  Extract facts  │
    │  Group updates  │
    │  Identify risks │
    └─────────────────┘
               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      OUTPUT PHASE                                │
└─────────────────────────────────────────────────────────────────┘
               ▼
    ┌─────────────────────────────────────────────┐
    │          Structured Markdown Report          │
    │                                              │
    │  ## Site: [Name]                            │
    │  ## Date: [DD/MM/YYYY]                      │
    │                                              │
    │  ### 1. Overall Site Status                 │
    │  [Executive paragraph]                      │
    │                                              │
    │  ### 2. Work Completed Today                │
    │  - Achievement 1                            │
    │  - Achievement 2                            │
    │                                              │
    │  ### 3. Issues / Delays                     │
    │  - Problem 1                                │
    │  - Blocker 2                                │
    │                                              │
    │  ### 4. Risks / Attention Required          │
    │  - **Critical Risk** (bold)                 │
    │  - Concern requiring attention              │
    │                                              │
    │  ### 5. Tomorrow's Planned Work             │
    │  - Scheduled activity 1                     │
    │  - Meeting 2                                │
    │                                              │
    │  ### 6. Decisions Needed                    │
    │  - Awaiting approval 1                      │
    │  - Management input needed                  │
    └─────────────────────────────────────────────┘
               ▼
    ┌─────────────────┐
    │  Save as .md    │
    │  Ready to share │
    └─────────────────┘
```

## 🎯 Execution Paths

### Path 1: Complete Pipeline (Recommended)
```
python generate_report.py "input/chat.txt" "Site Name"
    │
    ├─► Parse messages
    ├─► Validate quality
    ├─► AI summarization
    └─► Save both JSON and MD
```

### Path 2: Parse & Review (Cautious)
```
python run.py "input/chat.txt"
    │
    ├─► Parse messages
    ├─► Preview first 10
    └─► Save JSON
            │
            ▼
Review JSON manually
            │
            ▼
python summarizer.py "output/chat_parsed.json" "Site Name"
    │
    ├─► AI summarization
    └─► Save MD report
```

### Path 3: Batch Processing (Multi-site)
```
Loop through input/*.txt
    │
    ├─► Parse each file
    ├─► Generate report for each
    └─► Organize by site/date
```

## 🔍 Data Flow

```
Raw WhatsApp .txt (235 lines)
    │
    ├─ Remove system messages (-10 lines)
    ├─ Filter encryption notices (-3 lines)
    ├─ Clean Unicode artifacts
    ├─ Merge multi-line messages (-73 lines)
    │
    ▼
Clean JSON (149 messages)
    │
    ├─ Format for AI (~5000 tokens)
    ├─ Add prompt + structure (~1000 tokens)
    │
    ▼
AI Processing (~6000 input tokens)
    │
    ├─ Extract facts
    ├─ Categorize by section
    ├─ Group similar updates
    ├─ Highlight risks
    ├─ Format professionally
    │
    ▼
Structured Report (~1500 output tokens)
    │
    └─ Professional EOD report (1 page, 6 sections)
```

## 📊 Quality Gates

```
Gate 1: Input Validation
   ├─ File exists?
   ├─ Valid encoding?
   └─ WhatsApp format?
           │
           ▼ PASS
Gate 2: Parsing Validation
   ├─ Messages extracted?
   ├─ Timestamps valid?
   ├─ No garbage?
   └─ Preview looks good?
           │
           ▼ PASS
Gate 3: API Validation
   ├─ API key set?
   ├─ Credentials valid?
   └─ Provider available?
           │
           ▼ PASS
Gate 4: Output Validation
   ├─ Report generated?
   ├─ Structure correct?
   ├─ Length appropriate?
   └─ Facts grounded?
           │
           ▼ PASS
   ✅ Production Ready
```

## ⚡ Performance

```
Input: 200 messages
    │
    ├─ Parse: ~0.1s (instant)
    ├─ Format: ~0.01s (instant)
    ├─ AI API call: ~3-8s (network dependent)
    ├─ Save output: ~0.01s (instant)
    │
    ▼
Total: ~3-10 seconds per report
```

## 💡 Decision Tree

```
Start
  │
  ├─ Have WhatsApp export? ──NO──► Export chat from WhatsApp
  │                            │
  ├─ Yes                       │
  │                            ▼
  ├─ API key set? ──NO──► Run: check_setup.py
  │                    │       │
  ├─ Yes               │       ▼
  │                    └─► Follow SETUP.md
  │
  ├─ First time? ──YES──► Test with sample file
  │              │
  ├─ No          ▼
  │         Verify output quality
  │              │
  │              ▼
  ├─ Multiple files? ──YES──► Use batch script
  │                   │
  ├─ No               ▼
  │              Process all at once
  │
  ├─ Need to review parsed data? ──YES──► Use two-step workflow
  │                                │
  ├─ No                            ▼
  │                           run.py → review → summarizer.py
  │
  ▼
Use generate_report.py (one command)
  │
  ▼
✅ Done! Report ready
```

---

**Key Principle**: Clean input → AI processing → Structured output

**No garbage in = Professional report out**

