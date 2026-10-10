# void-lab

> Curious about how things work and what's possible.
> Learning by building and experimenting.

## About

I'm Dani Sam (voidhyr), an aspiring software engineer. This lab documents my
practice, experiments and lessons learned.

I'm interested in computer systems, efficient computing and WebAssembly. I'm
learning Rust through small projects, and I still use Python for tools, data
scripts and charts. Earlier work here is mostly Python, and I've kept it as a
record of how I got here.

I want to build useful software, understand it deeply and explore how
computing can become more accessible to people with limited resources. My
direction may change as I learn.

## Currently Learning & Exploring

| Area | Current focus |
| --- | --- |
| Rust | Ownership, structs, collections, testing and Cargo |
| WebAssembly | Running Rust in the browser |
| Computer systems | Performance, measurement and how programs use the CPU |
| Maths | Linear algebra and statistics, alongside practical work |
| Python | Tools, data scripts, testing and plotting results |

These are learning directions, not claims of mastery or completed research.

## Learning Path

1. **Learn Rust by building a small project.** Write code I can explain,
   modify and debug myself.
2. **Run the same code natively and in the browser.** Learn how WebAssembly
   builds work and where they differ.
3. **Measure, don't assume.** Separate the work being timed from everything
   else, repeat measurements and report ranges honestly.
4. **Study maths alongside code.** Use small examples and plots.
5. **Keep Python as a supporting tool.** Use it for scripts, data handling and
   charts.
6. **Explore through experiments.** Ask clear questions, record what happened
   and say what the results do and don't show.

These stages overlap. I don't need to master every topic before building.
Git, Linux, debugging and documentation are part of the process throughout.

## Projects

### mote (in progress)

A small 2D particle simulation written in Rust, intended to run both natively
and in a web browser through WebAssembly. It is a learning project: the goal is
a finished, understandable result with a README that explains how it works and
its limitations.

[Browse mote](projects/mote/)

### Books to Scrape (learning project)

A Python scraper using HTTPX, BeautifulSoup and SQLite to collect book titles,
links, prices, ratings and availability from Books to Scrape.

The next milestone is a reliable small version: correct extraction, separate
parsing and execution, handle failures, test with local HTML samples and verify
duplicate-safe database updates. These are improvement goals, not a statement
that every item is already complete.

[Browse the scraper](projects/books-to-scrape/)

## Repository Structure

```text
void-lab/
├── projects/
│   ├── mote/              Rust and WebAssembly simulation (in progress)
│   └── books-to-scrape/   Python scraper with SQLite storage
├── fundamentals/
│   ├── python/            Python practice exercises and small scripts
│   ├── rust/              Small Rust exercises while learning the language
│   └── dsa/               Data structures and algorithms exercises
├── archive/               Earlier work kept for reference
└── README.md
```

| Folder | Purpose |
| --- | --- |
| `projects/` | Projects I'm building or improving, each with its own README |
| `fundamentals/python/` | Introductory and intermediate Python practice: basics, collections, loops, OOP, patterns and small games |
| `fundamentals/rust/` | Small Rust exercises and notes, one Cargo project per exercise |
| `fundamentals/dsa/` | Searching, sorting, graph algorithms and other exercises |
| `archive/` | Earlier projects retained for reference |

Additional folders will be introduced when they contain actual work.

## Tools

- **Main language (learning):** Rust
- **Supporting language:** Python, with NumPy, Pandas and Matplotlib
- **Data and storage:** SQL and SQLite
- **Development environment:** Ubuntu/Linux, Neovim, Git/GitHub
- **Python environments:** uv

## Working Principles

- Build small, useful programs before expanding their scope.
- Understand code well enough to explain, change and debug it.
- Use AI assistance thoughtfully; verify its output and document assistance where relevant.
- Prefer simple approaches when they solve the problem adequately.
- Measure performance rather than assuming it.
- Write tests for meaningful behaviour, including failure cases.
- Respect source access rules and rate limits when collecting data.
- Document setup, limitations, results and lessons learned.
- Report unsuccessful experiments honestly and distinguish evidence from assumptions.

## Connect

[**Enter the Void → Personal Site**](https://voidhyr.github.io/Personal-Website/)

[Articles](https://dev.to/voidhyr) · [X](https://x.com/voidhyr)

_Build it. Question it. Understand it._
