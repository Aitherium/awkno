# awkno — The man page for the Aither World

<!-- aither-header:start GENERATED from the ecosystem registry. Edits here are overwritten; change the registry instead. -->

**[Docs](https://aitherium.github.io/awkno/)**  ·  [Source](https://github.com/Aitherium/awkno)  ·  `pip install awkno`  ·  [The Aither World](https://aitherium.github.io/)

> **The Aither World** is an operating system for agents — a Linux you can hand to one, the runtimes it works in, and the tools it works with. [awnix](https://github.com/Aitherium/awnix) is the Linux underneath it; **awkno** is one of its 72 bricks — each installs on its own, runs offline, and needs no account. 6 more are in development and 23 are planned.
>
> **Start here:** Ask it what a brick does and get the answer with your network cable out.

<!-- aither-header:end -->

**Every brick, stack, and law in your terminal, offline.**

awkno is a standalone reference for the Aither World ecosystem — the set of portable, composable tools and principles that make agent automation reproducible and auditable. No browser, no internet connection, no external dependencies needed.

## Why

Agent systems need documented principles. The Aither World is built on 32 laws derived from real failures on production systems — lessons about gates, silence, atomicity, and delivery that apply to every agent work you build.

The ecosystem itself is <!-- awkno:stats -->74 bricks · 29 stacks · 32 laws<!-- /awkno:stats -->. awkno brings them all into your terminal: any brick's purpose and adoption path, any law's principle and reasoning, any stack's composition and status — all offline, all fast, queryable by keyword, and open to reading and redistribution.

## Quick Start

### Install

```bash
pip install awkno
```

### Use

```bash
# Show a brick
awkno awdk
awkno awsh

# Show a law
awkno law 5

# List everything
awkno list

# Search for a term
awkno search agent
awkno -k silence

# Raw output for piping
awkno awdk --plain
awkno --json awdk
```

### No Arguments

```bash
awkno
```

Shows the overview: command summary, quick start examples, and how to explore further.

## What's Inside

### Bricks

<!-- awkno:bricks -->
- **AitherConnect** — Browser extension
- **AitherZero** — PowerShell 7+ automation framework
- **aitherkvcache** — Near-optimal KV cache quantization for LLM inference
- **awask** — Your agent asks you a question
- **awasp** — Stream a multi-gigabyte model onto a device that cannot hold it all at once
- **awavatar** — One character spec in, a rigged, animated, multi-style avatar pack out
- **awbac** — Role-based access control that fails closed and explains itself
- **awbeads** — A spatial canvas for a page
- **awbonsai** — Run a real model in the visitor's own browser
- **awbrain** — Your history as a wiki of linked markdown
- **awbrowse** — A portable browser client
- **awclassify** — Classify any document -- what it is, who may read it, who it is for, what it is about
- **awdecide** — One typed-decision contract -- choice / score / bool with a probability -- over a ladder of backends you already run (rules, tiny local models, an LLM's logprobs), fail-closed, with a Brier ledger that resolves every decision against its outcome
- **awdelphi** — Anonymous multi-round expert panels
- **awdesk** — Aither World Desk -- the desktop body of AitherOS Online: tray, avatars, decision cards, the Living Desktop as an overlay
- **awdiscord** — Put any agent on Discord as a real bot, with an operator in the loop
- **awdit** — An append-only audit trail whose gaps are DETECTABLE
- **awdk** — Build AI agent fleets
- **awedgerunner** — Run agent and CI work on edge runners nobody has to rack -- a volunteer's idle GPU, a phone on your own mesh, an edge worker, a free or spot CI runner -- under a lease with a hard budget cap, a named payer and an expiry
- **awembed** — Train an embedding model that knows your corpus, and prove it beats the big one
- **awevolve** — Point an agent at a file and a command that scores it, and let it improve
- **awfind** — A portable search client
- **awflow** — A deterministic workflow runtime
- **awfocus** — See, search and steer every Claude session from one command
- **awgit** — Semantic version control on top of git
- **awgraph** — A semantic code graph for agents
- **awgym** — An ARC training gym
- **awiam** — Who is this caller? A directory and session store that fails honestly
- **awindex** — A curated, git-backed map of the internet
- **awkit** — Render an agent panel from a tool result
- **awkno** — The man page for the Aither World
- **awknowledge** — How to run a coding agent so the result survives
- **awm** — A portable, scoped agent memory
- **awmail** — Give an agent an email address
- **awmine** — Mine what your agents did -- outcomes, lessons and procedures out of the transcripts they left behind
- **awnboard** — A front gate you can put in front of anything, and hand someone the key to
- **awnest** — Prove there is a human before you let them into the nest
- **awnet** — The agentic web
- **awnix** — A Linux you can hand to an agent
- **awnode** — A lightweight local gateway
- **awpack** — First-party agent packs
- **awpermit** — Let an agent through your door with a scope, a spend cap, and someone accountable
- **awpool** — The free half of the elastic work pool: dispatches public-safe work onto the free GitHub-hosted runners of the public aw* mirrors, so their idle CI minutes become compute. awrun remains the paid/self-hosted lane; this is its free twin
- **awpredict** — Predict what your environment does next, and how surprised you were
- **awprism** — Turn a failure into ranked hypotheses
- **awreason** — A portable reasoning client
- **awrecover** — Labelled snapshots with an all-or-nothing restore
- **awrecurse** — Answer a question over a context far larger than the window
- **awrelay** — Portable agent messaging
- **awrena** — Put two agents head to head and get a verdict you can check
- **awrepl** — A REPL an agent can actually use
- **awreport** — File a bug report that has already scrubbed your secrets and collapsed the duplicate
- **awresearch** — Ask a research question, get a cited report you can check
- **awrise** — Wake an agent on a schedule, let it do one thing, and put it back to sleep
- **awrouter** — OpenRouter for your own fleet: pick a model backend by cost/latency/ capability, fail over, fit the context window, stream. Standalone, OpenAI-compatible, no Aither-specifics required to be valuable
- **awrtifact** — Deliberately chunk artifacts into GitHub release assets
- **awrun** — A priority-aware queue and dispatcher for agentic runs and ad-hoc CI builds. It also judges whether the runner pool is big enough for the queue it is draining, and can ask a host to grow it -- reserving capacity is zero-sum, so a saturated pool needs more of it, not a different share of it
- **awscreen** — See this machine
- **awseal** — Sign an artifact so a stranger can verify it
- **awsettings** — Your agent's permissions and config, following you to the next machine
- **awsh** — Your terminal answers you -- type a question where a command would go
- **awshare** — Publish an artifact and fetch it back verified
- **awskills** — Portable agent skills
- **awsprite** — Hatch a companion that grows only from what you teach it, then take it home
- **awstorage** — Every drive on every node, indexed, classified and diffed -- so you can see what you own before you delete it
- **awsuite** — Your Google Workspace as agent tools, and no write happens without a yes
- **awswarm** — Run one model too big for any single GPU across a pool of small ones
- **awtax** — Turn any tax PDF -- returns, W-2, 1099, statements, even scans -- into structured data you can check
- **awtoll** — What every tool call costs you in context, measured from your own transcripts
- **awtunnel** — Reach a service that has no public address
- **awvision** — See an image
- **awvoice** — Hear and speak
- **awwall** — Say what a workload may reach, and watch everything else fail closed
- **gawbbonet** — GobboNet campaigns with a real agent brain
<!-- /awkno:bricks -->

Portable, single-purpose tools that do one job well and compose with others.


Each has an "adopt" sentence: the smallest useful thing you can do with it alone, without adopting anything else.

### Stacks

<!-- awkno:stacks -->
- **agent-senses** — What an agent needs to perceive things outside its own process. Search and pages are the two it has; voice, vision and the screen in front of it are the three it does not, and they are named here so they stop being rediscovered as absences.

Includes: awfind, awbrowse, awvoice, awvision, awscreen, awdk
- **agent-vm** — awnix already carries the capabilities; adding an agent is three lines in a Dockerfile, and your skills and credentials layer on top of that. The point of the order is that the guarantees live in the base, so swapping the agent keeps them.

Includes: awnix, awdk, awskills, awkno, awsettings
- **agentic-orchestrator** — The substrate a cluster orchestrator gives agent workloads, as bricks a stranger adopts one at a time on one machine: awrun is the unit of work (priority, suspend, resume, declarative apply, limits and egress that FAIL CLOSED); awflow is why a resumed run continues instead of restarting (the journal is the checkpoint, finished model calls replay); awrise is the clock; awrouter and awnode decide which model answers; awdk is the agent loop and awrepl its live session; awnix is the machine. Governance is not a later phase: awiam says who, awbac says whether, awdit records it before it happens, awseal signs a run that leaves the machine and awshare verifies the one that arrives. Registered 2026-09-21 when a cluster-native agent orchestrator was announced and the question "did we already build this" had no single place to be answered from.

Includes: awrun, awflow, awrise, awrouter, awnode, awdk, awrepl, awnix, awiam, awbac, awdit, awseal, awshare
- **avatar-ensemble** — Spawn more than one Persona-driven avatar at once, bind each to a distinct awdk agent persona (its own Library/pack, its own model), render them together in one shared scene, and let them hold a live concurrent conversation with each other and the owner -- steered from awsh as the cockpit. Registered 2026-08-24 per: "give an avatar a face and a mind, then let several of them talk" cannot be said without naming the companion, the agent runtime and the shell that steers it, so this is a stack over existing bricks, not a new brick (same reasoning as `awsprite`, which this stack composes with directly).

Includes: awdk, awsh, awvoice, awvision, awsprite, awdesk
- **aws** — An open-source private cloud you run yourself: identity, directory, RBAC, secrets, certificates, object storage, events, metrics, audit, messaging, jobs and tunnels, on an immutable awnix base on hardware you own. The parts a stranger can adopt alone are these bricks. The control plane behind them (Identity, Directory, Secrets, Strata, Flux, Pulse, Watch, Chronicle, Nexus, Relay) is a set of platform services that the sovereign-replica layer set stands up, not bricks. Solutions (CRM, mail, web hosting, MDM, the OccupySaaS packs) ship as optional packs on top and are never baked in.

Includes: awnix, awdaemons, awrun, awiam, awbac, awdit, awseal, awrelay, awtunnel, awpack
- **browser-companion-graduation** — Owner directive 2026-08-24, reinforcing the existing AitherSprite Phase 2/3 roadmap (the product architecture doc and the knowledge-companion program doc): AitherSprite today is playable but shallow -- flat per-sprite knowledge rows, titles-only in the talk prompt, server-side inference only, and "download it" is a paid pack with no guided path to actually WIRE it to real local tools and data. The directive is four upgrades composed together, and none of the four pieces is new -- the gap is that nothing connects them for this product: teaching should build a real personal knowledge GRAPH (`awgraph` is a CODE graph today -- CodeChunk/CodeGraph/CodeGraphStore -- and `awm` is scoped FACTS, not a traversable graph; a per-user knowledge graph does not exist as a brick yet); the companion should run and be TRAINABLE fully in-browser on `awbonsai`, not only through a server round trip; and graduating a companion should walk the owner through a real self-service CONNECT of `awdk` + `awsh` + `awnode` on their own machine -- the same shape as the self-host guide's stranger-to-provider flow, but ending in "your companion can now use your files/tools" instead of "your GPU now serves the mesh". NOT a rewrite of the companion engine -- its deterministic core (needs/mood/evolution, no I/O) is correct and stays the server-authoritative source of truth even for a browser-trained companion, so growth cannot be forged client-side (a fail-closed gate is not optional). What changes is WHERE teach/talk execute (in-tab via `awbonsai` when offline or pre-account, server via MicroScheduler when connected) and how knowledge is stored (a graph, not a flat table).

Includes: awsprite, awbonsai, awdk, awsh, awnode
- **cited-research** — A research question answered against real sources, where the report names what it read (awresearch), the sources are found and actually opened rather than hallucinated (awfind, awbrowse), and what was learned survives the session (awm). The one failure this set exists for is the plausible document: fluent, well-formed, citing pages nobody fetched.

Includes: awresearch, awfind, awbrowse, awm
- **creator-stack** — One world that runs, not a text box that continues — with a story graph, typed mechanics, a continuity checker, MCTS branch explorer, simulation backend, and persistent memory. One creative studio with 357 routes and 137 named ops — character rigs, animation, LoRA, comics, VN, production loops with human gates — all agent-callable. One visual artist that plans, enhances, calls the studio in a real loop, evaluates and refines. Run it all on your box with awdk + awnode + Bonsai, or on the cloud with the same key. Sold as credits and subscriptions; created work published to the marketplace with revenue share.

Includes: awsaga, mediaforge, awiris, awsprite, awdesk, awbonsai, awdk, awnode, AitherConnect, awrtifact
- **dark-matters-living-world** — Procedurally generate a playable, persistent-realm 3D world -- zones, quests, living NPCs on a decide-door mind stack, creatures, their bodies, rigs, clips and style renders -- from Saga narrative and Prometheus balance, hosted by the Dark Matters engine (the CoC story engine grows the world; owner decision 2026-09-21) with the World of ClaudeCraft-derived realm as the PG public world and sim donor, and the same character carried into awdesk and a Space.

Includes: awavatar, awdk, awdecide, awsprite, awrtifact, awrun
- **inference-commons** — Owner directive 2026-09-01: decentralise storage and inference across the aw* stack so anyone's node can join the mesh, share models and resources, and pool inference -- including cross-model KV-cache sharing across nodes. Registered because each plane is real INSIDE the fleet and absent at the public boundary: the overlay (AitherMesh + Conductor onboarding) is deployed and `awnet` fronts it; `awnode` routes to a warm peer; same-model warm-prefix sharing exists as llamacpp_connector + kv_catalog (Nexus) + Strata as the cold tier; cross-model maps exist as lib/gpu/kvtransfer; `awswarm` holds the sub-layer placement math; `aitherkvcache` quantises the cache; `awrtifact` ships the packs; `awnix` is the box a contributor boots. What no brick does yet is let a STRANGER'S node discover a warm prefix, receive a mapper pack, or get settled for serving -- `awcache` is the first of those three; settlement is the external OmniNode plane.

Includes: awnix, awnode, awnet, awswarm, awpool, aitherkvcache, awrtifact, awtunnel, awwall, awedgerunner
- **mine-what-you-ran** — The owner's ask, 2026-09-20: mine Claude Code and other agent terminal sessions automatically and turn what they contain into agent packs, skill packs, tool packs, RL outcomes, world-model and awpredict training, AitherCNS state and ARC-solver evidence. awmine reads the transcripts (it is the miner AitherHarvest never had for this source -- measured that day: 954 transcripts changed, zero mined); awtoll prices them; awm keeps the lessons; awdata holds the labelled corpora; awdecide is taught every tool outcome; awskills and the awdk toolpacks are where a repeated procedure becomes a pack; awrise is the wake that runs it on a schedule and records that it ran. The fleet's AitherHarvest, Trainer, Evolution and CNS are CONSUMERS of what awmine emits, never the miner.

Includes: awmine, awtoll, awm, awdecide, awskills, awdk, awrise
- **one-surface** — OWNER DECISION 2026-08-19, recorded because it was made in a transcript and would otherwise be re-litigated: stop hand-maintaining a web UI per app. The Living Desktop is the shell; an "app" is a dynamic agent panel rendered from a tool result (awkit), scoped by the identity plane, driven by intent rather than clicking. veil/portal keep serving pages and APIs where genuinely needed -- the UI, widgets and apps are what collapses, not the hosting. WHY, measured that day on ONE tenant: 18 apps listed and 0 deployed; AitherOne showing "Service Unavailable" while healthy, because all 11 of its GET routes require a body and answer 422 to every caller alive; 189 catalogue routes against 105 registered panels; and 2 of 6 declared panels were ids with NO component -- rendering nothing, with no error, no boundary and no log line. Every one of those is the same shape: declared in one place, not real in another, and nothing comparing the two. THE TRAP THIS MUST NOT INHERIT, stated here so the stack is judged on it: collapsing six surfaces into one does not fix that shape, it reduces how many places it can happen. A panel spec a renderer cannot honour is a stale component one layer up. The parity gate (-'s shape: producer ids == renderer ids, asserted by something that fails) comes FIRST, or this becomes the seventh island. DONE means: one previously-broken app rebuilt as an agent panel end to end with real scope and real data; the entitlement plane answering once instead of a catalogue and a backend disagreeing; and surfaces retired by the ratchet, one at a time, each with its consumers moved in the same commit -- never by decree.

Includes: awkit, awdk, awnode, awiam, awbac
- **open-scheduler** — MicroScheduler for someone else's agents, as three bricks a stranger adopts alone: awrouter decides which backend serves model X right now (the STATELESS routing plane extracted from AitherMicroScheduler.py -- 19,535 lines / 107 imports, never lifted), awrun is the durable priority queue, awrise is the clock that wakes work and records what happened. awnode is the local gateway an app points at instead of a vendor URL; awdk is the loop that runs on top. The stateful platform half (budgets, heartbeats, throttling, agents) stays inside the fleet and CONSUMES these. Registered 2026-09-19 because the owner asked 'how are we open-sourcing MicroScheduler' and the answer was already three registered bricks that no stack named together.

Includes: awrouter, awrun, awrise, awnode, awdk
- **personal-agent-home** — Owner directive 2026-09-21, the day Meta announced Muse: the same journey has to compose HERE from bricks a stranger can install -- a desk body (awdesk) that hosts the aitherium.com Living Desktop over the real desktop and embodies an agent as an avatar; the browser body (AitherConnect) that puts the same overlay over any page; a companion (awsprite) that grows a knowledge base from what its owner teaches it, remembered in awm, built and grown with awdk packs; self-service self-hosting (awnix / awnode / awsh) so the whole thing runs on the owner's own box; device registration through a front gate (awnboard + awiam); and tunnels between those devices that the PLATFORM cannot read. Every seam was measured, not assumed: awdesk already loads aitherium.com/?mode=overlay and reuses AitherConnect's overlay-mode protocol; awdesk registers a local MCP server so awsh/adk can drive it; device enrolment lives in a tenant backend (`devices.py`) and the tenant node table (`/tunnel/tenant/{t}/nodes`). What did NOT hold on 2026-09-21: every tunnel enrolment path minted the device's WireGuard private key SERVER-SIDE and `_save_peers` persisted it to the vault, so the platform could read any device's tunnel -- fixed the same day (bring-your-own public key on every enrolment endpoint, device private keys never persisted; `test_tunnel_key_custody.py`). Owner-blind device-to-device tunnels already exist and are the DEFAULT: `adk join` (awdk/adk/commands/join.py) brings the node up on the headscale tailnet (`hs.aitherium.com`, /health 200 on 2026-09-21) with a mesh key minted by Identity -- node keys are generated on the device, traffic is peer-to-peer WireGuard, and the control plane sees public keys only. The AitherTunnel hub VPN is the lane for reaching platform services and dev workspaces; it terminates at the hub by design. Still `partial` because awsprite is `planned` and mobile chat is Discord-only.

Includes: awdesk, AitherConnect, awsprite, awdk, awm, awkno, awknowledge, awnboard, awiam, awtunnel, awnet, awnode, awnix, awsh
- **personal-mesh-pool** — Owner directive 2026-08-24: someone with a laptop, a desktop and a phone should be able to join their OWN devices into one pool and have a model stay warm and servable across whichever of them is on, without joining the platform's shared AitherNet compute market. Registered here because it does not exist yet, and the three pieces that would compose into it are each individually real: `awnet` is a peer REGISTRY + three-valued TCP reachability check ("is anyone listening") -- explicitly not a VPN and not a placement/pooling primitive, by its own README; `awnode` is the local gateway that would route a request to whichever peer has the model warm; `awdk` is the runtime that would run on each device. None of the three knows about model PLACEMENT or WARM-KEEPING across peers today -- that logic is the actual gap, not the transport (mesh-deploy/WireGuard already exists for that) and not per-node serving (node-bootstrap already detects hardware and stands up a local backend). The closest existing precedent is the platform's own DGX+5090+RTX ggml-RPC pooled-inference stack, run at fleet scale and never packaged as something a customer's own device fleet can stand up for itself. NOT `aithernet-provider` (that joins the PLATFORM's community pool with settlement -- a different shape) and NOT a rename of the fleet's pooled-inference stack (/client-not-lift: that stack is thousands of lines of fleet-specific orchestration; a personal-pool brick would be a small client speaking to whichever peers `awnet` says are reachable, same relationship as `awrelay` to `AitherRelay.py`). SHARPENED 2026-08-24, owner asked to "start serving all of our model stack from the mesh pool for flexibility": the ggml-RPC precedent is NOT a general placement layer and generalising it directly would be the wrong move -- it does TENSOR-LEVEL SPLIT serving for ONE model too large for any single box (DeepSeek-V4-Flash, 97-108 GB, routed experts pinned to the DGX's 121 GB by design), hand-tuned per model (custom RPC server build, per-backend thread counts, a dedicated watchdog/alerting stack -- see `pooled-inference-ops` skill). Bonsai/Qwen3.8/gemma4 do not need splitting, they fit one GPU each; what they need is PLACEMENT (which box, right now) plus WARM/PARK lifecycle across many small models competing for few GPUs -- a different problem the RPC pool was never built to solve. The real placement layer already exists in shape (`AitherCompute`'s `gpu_power_state` -- hot/parked/on_demand, idle-reap) but is currently DEAD fleet-wide (: no docker socket reachable from its container) -- so today NEITHER the platform's own stack nor a customer's personal pool has a working dynamic-placement layer; the gap is the same gap at two scales.

Includes: awnet, awnode, awdk
- **provenance** — Prove what an artifact is, who acted on it, and that nothing was quietly removed from the record.

Includes: awseal, awshare, awdit, awbac
- **retrieval-you-trained** — The searching tools are only as good as the vectors under them. awembed trains the embedder on your corpus and proves it on held-out directories; awgraph, awfind and awm then search, rank and remember over vectors that know your code instead of someone else's. awdk agents consume all of it as tools. awdata carries the labelled corpora the proving is done against -- the half that usually never ships, and the half that decides the answer: the same compression measured -0.006 macro-F1 on source files and -0.10 on real Reddit comments.

Includes: awembed, awgraph, awfind, awm, awdk
- **set-and-forget** — What a scheduled agent needs so that "it ran" is a fact and not a hope: a host clock that wakes it (awrise), a durable queue it hands work to (awrun), a line a human can read when a wake goes wrong (awrelay), a card when a wake needs a decision (awask), and the agent that gets woken (awdk). Named 2026-09-18 because every member exists and every one was proposed as the place the schedule should live; the measurement said the clock is the OS's and the brick's job is the memory.

Includes: awrise, awrun, awrelay, awask, awdk
- **shared-worktree** — Several agents editing one codebase without sweeping each other's work or re-deriving what the last one already learned.

Includes: awgit, awgraph, awrelay, awm
- **the-aither-way-claude-code** — Claude Code with the family wired in, each piece taken on its own: a plugin that makes any harness a native subagent, scoped memory recalled at session start, peer findings delivered in-turn, a code graph and a finder as MCP servers, a shared-worktree git that commits only your paths, a spoken reply on Stop, a settings preset that keeps portable and machine-local settings apart, and the doctrine and skills an agent loads on demand. Every surface is listed per brick under `In Claude Code` and is generated from this registry.

Includes: awdk, awsh, awsettings, awskills, awknowledge, awkno, awgit, awrelay, awm, awgraph, awfind, awfocus, awprism, awdecide, awvoice
- **the-daily-driver** — Using every agent, skill and fleet tool from a terminal without Claude Code. awsh is the door, the awdk harness daemon (:8362) is what it opens onto, awnode is the fleet behind it, awdesk's Console is the same door with a face, and the skills are read where they already live. Done when: `adk harness new --harness awdk --agent saga --skill gauntlet` answers as Saga following the protocol (LIVE 2026-09-21, 26 agents generated from config/identities); saga/vera/iris appear in awsh and the desk menu with no hand patch (LIVE); `awsh> /skills` prints host N | genesis N | gateway N | drift 0 (code landed, deploy pending); the desk Command pane routes @agent /skill through the daemon (not started).

Includes: awsh, awdk, awnode, awdesk, awskills
- **the-front-door** — Who may come in at all, before anything asks who they are: a human check whose verdict is bound to one door and one use, the identity it names, the authority it feeds, and a record of every refusal. Named because the four already existed as four separate answers to one question a stranger asks first.

Includes: awnboard, awnest, awiam, awbac, awdit
- **the-reasoning-loop** — The thinking core, kept apart from the senses and the hands on purpose. A hard question becomes a session with phases you can inspect (awreason); a failure inside it becomes ranked hypotheses with a falsifying check for each (awprism); and the check is actually RUN against live state rather than recalled (awrepl). Those three are the loop. It composes with `agent-senses` for what is outside the process and with `shared-worktree` for what is in the codebase — which is why neither set is repeated here.

Includes: awreason, awprism, awrepl, awrecurse
- **the-studio** — What a creative turn needs, on hardware the operator already owns: a way to find things, a way to read a page, a way to research with citations, and a way to actually render and master the result. Named because these kept being proposed as ONE product, and the measurement said they are three INPUT surfaces and one OUTPUT surface -- which composes and does not merge. Every member is adoptable alone; the stack is a suggestion.

Includes: awforge, awfind, awbrowse, awresearch, awm
- **train-what-you-run** — The closed learning loop (pillar 6) scheduled by the thing it improves. Every utterance->intent->tool->outcome and every ledger row (prediction vs what happened) is harvested (AitherHarvest /import/batch -- 5,151 lines / 32 imports, so a SINK on awrise, never a brick); the trainer fine-tunes the intent router and the decide door on it (AitherTrainer, 4,902 / 56, a consumer whose training routines become wakes); awlab scores it on a leaderboard the loop cannot edit; awevolve keeps or reverts (AitherEvolution's client) under AVO006; the result lands back in awdk intent.py and awrise's timeouts and intervals. Registered 2026-09-19, partial: every seam exists in-fleet, none is wired to a wake, and awlab is not yet a package.

Includes: awrise, awevolve, awdecide, awdk
- **trust** — What lets you hand the platform to an agent, and where to check it rather than take our word: who the caller is (awiam), what an admitted agent may do and spend (awpermit), and how a service with no public address is reached (awtunnel). The public page is https://aitherium.com/trust/ -- DNSSEC, TLS, HSTS, OIDC, auth.md, the vault, tenant scoping, the tunnel, the mesh, the agent-readiness scan and the honest list of third parties, each linked to live evidence and re-verified by a checker every four hours.

Includes: awiam, awpermit, awtunnel
- **wake-learning-loop** — Every wake becomes evidence: on start, awm recall hands the job its own history (what failed last, what fixed it); before an expensive wake fires, awpredict reads the ledger as an environment and says whether it will time out again; on finish, the row is remembered, and awevolve may tune interval/timeout under AVO006 (the scorer is never the mutable file). Registered 2026-09-19 at planned: fleet-gates timed out twice in its first day and both were predictable from row one; nothing was watching.

Includes: awrise, awm, awpredict, awdecide, awembed, awevolve, awdk
- **who-what-did** — The three questions every access decision needs answered separately: who is this caller, what may they do, and what did they actually do. Kept apart on purpose -- one component that answers all three is one component that can quietly answer all three wrongly.

Includes: awiam, awbac, awdit
- **workspace-bridge** — One integration, every surface. awsuite holds the Google Workspace client and one tool table; awdk loads it as a toolpack, awsh and Claude Code reach it as an MCP server, awskills carries the playbooks, and awpack ships the bundle to a tenant. Swapping the harness keeps the tools and the confirm gate.

Includes: awsuite, awdk, awsh, awskills, awpack
<!-- /awkno:stacks -->

Curated sets of bricks that work together.


### Laws

<!-- awkno:laws -->
1. A rule nothing asserts is a suggestion
2. Make it a check, not a ticket
3. Watch your gate fail
4. Mutate the test, not just the code
5. Design for the silence
6. A check that cannot run must not pass
7. The symptom names the innocent
8. A checker in the wrong place found nothing
9. Detection without delivery is not detection
10. A gate that floods gets switched off
11. Open green, ratchet down
12. Measure it again
13. Written is not deployed
14. You wrote it; that does not mean it ships
15. Generate, never copy
16. The defect lives in the union
17. Fail closed, then prove the happy path
18. Never trust the caller for an authorization decision
19. Count the closure, not the edge
20. A platform you cannot ship to is not supported
21. A cap that does not survive a restart is not a cap
22. Coordinated decisions need a channel humans can read
23. A mixture-of-experts model has two budgets, not one
24. The always-on context is a budget
25. A setting in a scope nobody reads does not exist
26. A hook on every call spends a latency budget
27. One sanction file, never scattered
28. A guard in one direction is half a guard
29. Portable is files and presets, never credentials
30. Lead with the next action
31. A deploy tree is served, never edited
32. Use the lane
<!-- /awkno:laws -->

Lessons learned in production, written down so they don't have to be re-derived.


## Architecture

### Offline-First Design

The corpus is **generated once** from `ecosystem.yaml` and `awknowledge/laws/`, then **committed as JSON data files** under `awkno/pages/`. After install, the package needs no external files or network.

This means:
- No runtime generation (fast startup)
- No external dependencies beyond stdlib
- Reproducible across machines and time
- Auditable: every page is in the repo

### CLI Features

- **Pager support**: Automatic pagination on TTY (via `$PAGER` or system default)
- **TTY-aware formatting**: ANSI bold headers only when connected to a terminal
- **Multiple output modes**:
  - `--plain` — No ANSI codes (safe for piping to other tools)
  - `--json` — Structured output for scripting
  - Default — Man-page-style formatted text
- **Fuzzy search**: Type something close, get ranked results
- **Command shortcuts**:
  - `awkno list` — Show all topics grouped by category
  - `awkno law N` — Show law by number
  - `awkno -k TERM` / `awkno --apropos TERM` — Search (like `man -k`)

### No Internal Leakage

This package is built for public distribution, and the corpus is GENERATED from
an internal registry -- so the generator strips, and the build then re-checks,
every category of internal detail: infrastructure hostnames, absolute paths from
the build machine, issue-tracker and quality-gate identifiers, and imports that
only resolve inside a private monorepo.

The point of scanning the *generated* corpus rather than the generator is that a
sanitiser is only as good as its last pattern. A page that slips through reads as
ordinary prose, so nothing downstream would ever notice.

## Development

### Regenerate the Corpus

```bash
python awkno/generate.py
```

The generator reads:
- `ecosystem.yaml` — The brick and stack registry
- `awknowledge/laws/*.md` — the laws

And writes JSON to `awkno/pages/`.

### Test Locally

```bash
pip install -e .
pytest

# Or run the CLI directly
python -m awkno.cli awdk
```

### Build and Publish

```bash
pip install build
python -m build

# Publish to PyPI
twine upload dist/*
```

## Integration

### In Your Own Code

```python
from awkno import AwknoRegistry

registry = AwknoRegistry()
page = registry.get("awdk")
print(page.render())

# Search
results = registry.search("agent memory")
for page, score in results[:5]:
    print(f"{page.topic}: {page.synopsis}")

# List by category
bricks = registry.list_by_category("brick")
laws = registry.list_by_category("law")
```

### As a Dependency

awkno has zero runtime dependencies (PyYAML is dev-only, for corpus generation).

```toml
[project]
dependencies = [
    "awkno",
]
```

## Contributing

Read a law, apply it, send a pull request. The package itself is small and well-documented.

Pages are generated from `ecosystem.yaml` and law files — edits to those files flow into awkno on the next generation.

## License

Apache 2.0. See [LICENSE](LICENSE).

## Further Reading

- Ecosystem index: https://aitherium.github.io/
- Laws and codex: https://github.com/Aitherium/awknowledge
- Portable skills: https://github.com/Aitherium/awskills
- AitherWorld reference: https://aitherium.com

---

**awkno** — read the principles once, apply them everywhere.

<!-- aither-ecosystem:start GENERATED from the ecosystem registry. Edits here are overwritten; change the registry instead. -->

## The aw family

Standalone tools that share one idea: **replace something you would otherwise have to _trust_ with something you can _check_.**

Each installs on its own, works offline, and needs no account.

| | instead of trusting | you check |
|---|---|---|
| [awdk](https://github.com/Aitherium/awdk) | a framework's idea of how your agents should run | one loop you can read, pointed at a backend you already pay for |
| [awskills](https://github.com/Aitherium/awskills) | that an agent knows your procedure | the procedure written down, versioned, and loadable by any agent |
| [awpack](https://github.com/Aitherium/awpack) | that the pack you want shipped inside somebody's SDK, under whatever licence that SDK happens to carry | the pack as its own versioned artifact, with its own licence, that any agent runtime can install |
| [awm](https://github.com/Aitherium/awm) | that memory stayed in its lane | tenant:user:project scopes, so a write cannot cross a boundary |
| [awdesk](https://github.com/Aitherium/awdesk) | that the agent is somewhere behind a browser tab | a tray icon, a face on your desktop, and the decision card that pops when it needs you |
| [awnode](https://github.com/Aitherium/awnode) | a vendor's cloud with every prompt | a local gateway routing to backends you chose |
| [awgraph](https://github.com/Aitherium/awgraph) | that grep found everything | an AST + tree-sitter call graph an agent can traverse |
| [awgit](https://github.com/Aitherium/awgit) | that no one else is editing this file | a lease, refused at commit time if you do not hold it |
| [awdelphi](https://github.com/Aitherium/awdelphi) | one agent's confident take on a decision | the round trace, the anonymity, and who dissents |
| [awclassify](https://github.com/Aitherium/awclassify) | a filename, a folder, or whoever last touched it | doc_type, visibility, audience and topics, with the evidence lines that decided each |
| [awdecide](https://github.com/Aitherium/awdecide) | a hosted classifier's probability that never learns whether it was right | the decision, its probability, and the calibration curve from your own resolved outcomes |
| [awtoll](https://github.com/Aitherium/awtoll) | that your tooling is saving you context | the measured token cost of each tool call, and what the alternative cost |
| [awseal](https://github.com/Aitherium/awseal) | that the artifact came from who you think | an Ed25519 seal — the key that verifies is not the key that forges |
| [awshare](https://github.com/Aitherium/awshare) | that the download is intact | content-addressed bundles, verified on fetch |
| [awsuite](https://github.com/Aitherium/awsuite) | that an agent holding your mailbox will not send on its own | every send, draft, upload and create returns a dry-run until confirm is true |
| [awpermit](https://github.com/Aitherium/awpermit) | that an admitted agent will only do what its owner meant | an Ed25519 permit naming the agent, the principal, the door, the actions and the cap |
| [awnest](https://github.com/Aitherium/awnest) | that there is a person on the other end | a verdict with evidence, where "we could not tell" is not "yes" |
| [awrena](https://github.com/Aitherium/awrena) | a leaderboard someone can edit, and votes nobody counted | a scored duel with both answers kept, and a result bound to them |
| [awnboard](https://github.com/Aitherium/awnboard) | a share link anyone who sees it can use | an invitation addressed to one person, for one gate, revocable |
| [awnix](https://github.com/Aitherium/awnix) | that the box is what you left it as | an immutable image you built, with atomic rollback |
| [awrecover](https://github.com/Aitherium/awrecover) | that the restore worked | a restore that fully lands or does not land at all |
| [awstorage](https://github.com/Aitherium/awstorage) | a du you ran last month, and a peers file that says 3 TB free | an inventory snapshot per node with a diff since the last one, and each tree classified re-fetchable or not |
| [awrelay](https://github.com/Aitherium/awrelay) | a SaaS in the middle of your agents | findings, alerts and coordination over your own transport |
| [awask](https://github.com/Aitherium/awask) | that anyone read the paragraph where you asked | the ask itself, with a button that steers the session that raised it |
| [awmail](https://github.com/Aitherium/awmail) | a mailbox somebody else can read | mail your agents send and receive over your own server |
| [awdiscord](https://github.com/Aitherium/awdiscord) | a self-bot on someone's account, or a bot that acts without asking | slash commands, rate limits, and approval buttons only your operators can press |
| [awswarm](https://github.com/Aitherium/awswarm) | that a model either fits your GPU or it doesn't run at all | a placement plan and an acquisition-probability estimate before you spend on a run |
| [awfind](https://github.com/Aitherium/awfind) | one vendor's idea of the web | results from whichever providers you configured |
| [awbrowse](https://github.com/Aitherium/awbrowse) | that the page said what you were told | the render, the DOM and the requests it made |
| [awvoice](https://github.com/Aitherium/awvoice) | that a cloud vendor may hold your audio | a transcript and a wav from a service you host |
| [awvision](https://github.com/Aitherium/awvision) | a filename and a caption somebody wrote | what a model actually reports about the pixels |
| [awscreen](https://github.com/Aitherium/awscreen) | a selector that was true when the page was written | the elements actually rendered, by what they look like |
| [awbeads](https://github.com/Aitherium/awbeads) | that a layout your users built survives the next deploy | the arrangement as data you can read back, diff, and hand to another surface |
| [awsprite](https://github.com/Aitherium/awsprite) | a chatbot with a face that resets every session | a knowledge base you can list, edit, and watch shape what it becomes |
| [awbonsai](https://github.com/Aitherium/awbonsai) | that inference always means a request left the machine | a WebGPU model answering on the tab's own GPU, with a consent record logged before it ever loaded |
| [gawbbonet](https://github.com/Aitherium/gawbbonet) | the model to keep a 300-message campaign coherent by itself | campaign facts recalled from scoped memory you can list and edit |
| [aitherkvcache](https://github.com/Aitherium/aitherkvcache) | a vendor's quantisation defaults | sub-byte KV cache kernels you can benchmark yourself |
| [awrtifact](https://github.com/Aitherium/awrtifact) | a hand-rolled split script and a hand-edited worker manifest | byte-verified parts in a release, served with Range + CORS, sizes asserted by a live gate |
| [AitherZero](https://github.com/Aitherium/AitherZero) | a pile of scripts nobody has numbered | numbered, discoverable automation with declarative playbooks |
| [AitherConnect](https://github.com/Aitherium/AitherConnect) | what a page tells your browser to do | a federated search and desktop bridge you host |
| [awreason](https://github.com/Aitherium/awreason) | a confident paragraph | the phases it went through, and every tool call it made to get there |
| [awrecurse](https://github.com/Aitherium/awrecurse) | that everything you pasted in was actually read | which slices it opened, and what it concluded from each |
| [awprism](https://github.com/Aitherium/awprism) | the first explanation that fits | the ranked alternatives, and the observation that separates them |
| [awrepl](https://github.com/Aitherium/awrepl) | what the agent believes the value is | the value, printed from the live session |
| [awreport](https://github.com/Aitherium/awreport) | that the report you pasted carried no token in it | a redacted report, and the duplicate it merged into instead of filing twice |
| [awresearch](https://github.com/Aitherium/awresearch) | a summary of pages nobody opened | every claim against the source it came from |
| [awfocus](https://github.com/Aitherium/awfocus) | twelve terminal tabs and a bad memory | one command that names every session, finds any transcript, and opens or steers the one you want |
| [awgym](https://github.com/Aitherium/awgym) | that a world model learned anything from the games it saw | transitions captured from real play, fed back, and the retrodiction score falling on grids it never saw |
| [awpredict](https://github.com/Aitherium/awpredict) | a model because it trained without erroring | its prediction against a self-updating lookup, on the rows that are actually novel |
| [awevolve](https://github.com/Aitherium/awevolve) | that your optimisation loop is finding anything | every version it kept, the score that version earned, and the edit that produced it |
| [awsh](https://github.com/Aitherium/awsh) | that you already know the name of the command | what it decided your line meant, before it acts on it |
| [awmine](https://github.com/Aitherium/awmine) | that a session's lesson survived the session | a row per outcome, a candidate per lesson, and the transcript line each one came from |
| [awrise](https://github.com/Aitherium/awrise) | that a scheduled agent ran at all, and ran exactly once | a durable record of every wake -- fired, skipped, overlapped or timed out -- each with its reason |
| **awkno** _(you are here)_ | that the docs site is up, or that you remember the family | the whole ecosystem in your terminal, with no network at all |
| [awwall](https://github.com/Aitherium/awwall) | that a service only talks to the hosts you think it talks to | an explicit egress allowlist, where a denial names the rule that denied it |
| [awembed](https://github.com/Aitherium/awembed) | a general-purpose embedder that has never seen your code | a held-out split of whole directories, scored teacher vs student vs int8 |
| [awtax](https://github.com/Aitherium/awtax) | a closed tax app's sealed file you can never read again | a plain, provider-neutral schema of every figure, with the page it came from |
| [awsettings](https://github.com/Aitherium/awsettings) | that you will remember to re-approve the same thing on every box you work from | one profile, unioned rather than overwritten, with the credentials left behind |
| [awavatar](https://github.com/Aitherium/awavatar) | a cloud 3D vendor's opaque task id | a manifest with a sha256, a licence and a rig-audit verdict per file |

[**awnix**](https://github.com/Aitherium/awnix) is the ground floor — A Linux you can hand to an agent — immutable x86_64 & ARM64 (aarch64) base, capabilities included.

## The Aitherium ecosystem

Every repository here is public. Each publishes an `aither-manifest.json` beside its page, so any surface can read every sibling's — the network is browsable from any node in it.

| repo | what it is | pages |
|---|---|---|
| [awdk](https://github.com/Aitherium/awdk) | Build AI agent fleets — 3 lines, any backend, local or cloud | [docs](https://aitherium.github.io/awdk/) |
| [awskills](https://github.com/Aitherium/awskills) | Portable agent skills — self-contained procedures an agent loads on demand | [docs](https://aitherium.github.io/awskills/) |
| [awpack](https://github.com/Aitherium/awpack) | First-party agent packs — the ones we build, versioned and installable on their own | [docs](https://aitherium.github.io/awpack/) |
| [awm](https://github.com/Aitherium/awm) | A portable, scoped agent memory | [docs](https://aitherium.github.io/awm/) |
| [awdesk](https://github.com/Aitherium/awdesk) | Aither World Desk -- the desktop body of AitherOS Online: tray, avatars, decision cards, the Living Desktop as an overlay | [docs](https://aitherium.github.io/awdesk/) |
| [awnode](https://github.com/Aitherium/awnode) | A lightweight local gateway — bridges your apps to the AI backends you chose | [docs](https://aitherium.github.io/awnode/) |
| [awrun](https://github.com/Aitherium/awrun) | A priority-aware queue and dispatcher for agentic runs and ad-hoc CI builds. It also judges whether the runner pool is big enough for the queue it is draining, and can ask a host to grow it -- reserving capacity is zero-sum, so a saturated pool needs more of it, not a different share of it | [docs](https://aitherium.github.io/awrun/) |
| [awpool](https://github.com/Aitherium/awpool) | The free half of the elastic work pool: dispatches public-safe work onto the free GitHub-hosted runners of the public aw* mirrors, so their idle CI minutes become compute. awrun remains the paid/self-hosted lane; this is its free twin | [docs](https://aitherium.github.io/awpool/) |
| [awedgerunner](https://github.com/Aitherium/awedgerunner) | Run agent and CI work on edge runners nobody has to rack -- a volunteer's idle GPU, a phone on your own mesh, an edge worker, a free or spot CI runner -- under a lease with a hard budget cap, a named payer and an expiry | [docs](https://aitherium.github.io/awedgerunner/) |
| [awgraph](https://github.com/Aitherium/awgraph) | A semantic code graph for agents — AST + tree-sitter, call graphs | [docs](https://aitherium.github.io/awgraph/) |
| [awgit](https://github.com/Aitherium/awgit) | Semantic version control on top of git — edit-ops and leases | [docs](https://aitherium.github.io/awgit/) |
| [awdelphi](https://github.com/Aitherium/awdelphi) | Anonymous multi-round expert panels — a converged answer with a trace | [docs](https://aitherium.github.io/awdelphi/) |
| [awclassify](https://github.com/Aitherium/awclassify) | Classify any document -- what it is, who may read it, who it is for, what it is about | [docs](https://aitherium.github.io/awclassify/) |
| [awdecide](https://github.com/Aitherium/awdecide) | One typed-decision contract -- choice / score / bool with a probability -- over a ladder of backends you already run (rules, tiny local models, an LLM's logprobs), fail-closed, with a Brier ledger that resolves every decision against its outcome | [docs](https://aitherium.github.io/awdecide/) |
| [awtoll](https://github.com/Aitherium/awtoll) | What every tool call costs you in context, measured from your own transcripts | [docs](https://aitherium.github.io/awtoll/) |
| [awseal](https://github.com/Aitherium/awseal) | Sign an artifact so a stranger can verify it | [docs](https://aitherium.github.io/awseal/) |
| [awshare](https://github.com/Aitherium/awshare) | Publish an artifact and fetch it back verified | [docs](https://aitherium.github.io/awshare/) |
| [awsuite](https://github.com/Aitherium/awsuite) | Your Google Workspace as agent tools, and no write happens without a yes | [docs](https://aitherium.github.io/awsuite/) |
| [awdit](https://github.com/Aitherium/awdit) | An append-only audit trail whose gaps are DETECTABLE | [docs](https://aitherium.github.io/awdit/) |
| [awbac](https://github.com/Aitherium/awbac) | Role-based access control that fails closed and explains itself | [docs](https://aitherium.github.io/awbac/) |
| [awiam](https://github.com/Aitherium/awiam) | Who is this caller? A directory and session store that fails honestly | [docs](https://aitherium.github.io/awiam/) |
| [awtunnel](https://github.com/Aitherium/awtunnel) | Reach a service that has no public address | [docs](https://aitherium.github.io/awtunnel/) |
| [awpermit](https://github.com/Aitherium/awpermit) | Let an agent through your door with a scope, a spend cap, and someone accountable | [docs](https://aitherium.github.io/awpermit/) |
| [awnest](https://github.com/Aitherium/awnest) | Prove there is a human before you let them into the nest | [docs](https://aitherium.github.io/awnest/) |
| [awrena](https://github.com/Aitherium/awrena) | Put two agents head to head and get a verdict you can check | [docs](https://aitherium.github.io/awrena/) |
| [awnboard](https://github.com/Aitherium/awnboard) | A front gate you can put in front of anything, and hand someone the key to | [docs](https://aitherium.github.io/awnboard/) |
| [awnix](https://github.com/Aitherium/awnix) | A Linux you can hand to an agent — immutable x86_64 & ARM64 (aarch64) base, capabilities included | [docs](https://aitherium.github.io/awnix/) |
| [awrecover](https://github.com/Aitherium/awrecover) | Labelled snapshots with an all-or-nothing restore | [docs](https://aitherium.github.io/awrecover/) |
| [awstorage](https://github.com/Aitherium/awstorage) | Every drive on every node, indexed, classified and diffed -- so you can see what you own before you delete it | [docs](https://aitherium.github.io/awstorage/) |
| [awrelay](https://github.com/Aitherium/awrelay) | Portable agent messaging — findings, alerts, coordination | [docs](https://aitherium.github.io/awrelay/) |
| [awask](https://github.com/Aitherium/awask) | Your agent asks you a question — and acts on your answer | [docs](https://aitherium.github.io/awask/) |
| [awmail](https://github.com/Aitherium/awmail) | Give an agent an email address — send, and actually receive | [docs](https://aitherium.github.io/awmail/) |
| [awdiscord](https://github.com/Aitherium/awdiscord) | Put any agent on Discord as a real bot, with an operator in the loop | [docs](https://aitherium.github.io/awdiscord/) |
| [awnet](https://github.com/Aitherium/awnet) | The agentic web — agents host a mesh, and agents join one | [docs](https://aitherium.github.io/awnet/) |
| [awswarm](https://github.com/Aitherium/awswarm) | Run one model too big for any single GPU across a pool of small ones | [docs](https://aitherium.github.io/awswarm/) |
| [awfind](https://github.com/Aitherium/awfind) | A portable search client — query, results, ranking | [docs](https://aitherium.github.io/awfind/) |
| [awbrowse](https://github.com/Aitherium/awbrowse) | A portable browser client — navigate, console, network, DOM, screenshot | [docs](https://aitherium.github.io/awbrowse/) |
| [awvoice](https://github.com/Aitherium/awvoice) | Hear and speak — transcribe audio, synthesize a voice | [docs](https://aitherium.github.io/awvoice/) |
| [awvision](https://github.com/Aitherium/awvision) | See an image — describe it, ask it a question, compare two | [docs](https://aitherium.github.io/awvision/) |
| [awscreen](https://github.com/Aitherium/awscreen) | See this machine — what is on screen, and where to click it | [docs](https://aitherium.github.io/awscreen/) |
| [awkit](https://github.com/Aitherium/awkit) | Render an agent panel from a tool result — one component, any React app | [docs](https://aitherium.github.io/awkit/) |
| [awbeads](https://github.com/Aitherium/awbeads) | A spatial canvas for a page — arrange things, connect them, and keep the arrangement | [docs](https://aitherium.github.io/awbeads/) |
| [awsprite](https://github.com/Aitherium/awsprite) | Hatch a companion that grows only from what you teach it, then take it home | [docs](https://aitherium.github.io/awsprite/) |
| [awbonsai](https://github.com/Aitherium/awbonsai) | Run a real model in the visitor's own browser — no server round trip, no upload | [docs](https://aitherium.github.io/awbonsai/) |
| [awknowledge](https://github.com/Aitherium/awknowledge) | How to run a coding agent so the result survives — the laws, with evidence | [docs](https://aitherium.github.io/awknowledge/) |
| [awbrain](https://github.com/Aitherium/awbrain) | Your history as a wiki of linked markdown — claims pinned to the evidence | [docs](https://aitherium.github.io/awbrain/) |
| [gawbbonet](https://github.com/Aitherium/gawbbonet) | GobboNet campaigns with a real agent brain — scoped memory, graph recall | [docs](https://aitherium.github.io/gawbbonet/) |
| [aitherkvcache](https://github.com/Aitherium/aitherkvcache) | Near-optimal KV cache quantization for LLM inference — sub-byte compression | [docs](https://aitherium.github.io/aitherkvcache/) |
| [awrtifact](https://github.com/Aitherium/awrtifact) | Deliberately chunk artifacts into GitHub release assets — the productized aitherkvcache mirror lane | [docs](https://aitherium.github.io/awrtifact/) |
| [AitherZero](https://github.com/Aitherium/AitherZero) | PowerShell 7+ automation framework — numbered, self-describing scripts | [docs](https://aitherium.github.io/AitherZero/) |
| [AitherConnect](https://github.com/Aitherium/AitherConnect) | Browser extension — federated AI search, page context, and the Living OS overlay | [docs](https://aitherium.github.io/AitherConnect/) |
| [awreason](https://github.com/Aitherium/awreason) | A portable reasoning client — sessions, phases, thoughts, and the chain that produced the answer | [docs](https://aitherium.github.io/awreason/) |
| [awrecurse](https://github.com/Aitherium/awrecurse) | Answer a question over a context far larger than the window — recursively, with the trace kept | [docs](https://aitherium.github.io/awrecurse/) |
| [awprism](https://github.com/Aitherium/awprism) | Turn a failure into ranked hypotheses — and say what would confirm each one | [docs](https://aitherium.github.io/awprism/) |
| [awrepl](https://github.com/Aitherium/awrepl) | A REPL an agent can actually use — state that survives between turns | [docs](https://aitherium.github.io/awrepl/) |
| [awreport](https://github.com/Aitherium/awreport) | File a bug report that has already scrubbed your secrets and collapsed the duplicate | [docs](https://aitherium.github.io/awreport/) |
| [awresearch](https://github.com/Aitherium/awresearch) | Ask a research question, get a cited report you can check | [docs](https://aitherium.github.io/awresearch/) |
| [awfocus](https://github.com/Aitherium/awfocus) | See, search and steer every Claude session from one command | [docs](https://aitherium.github.io/awfocus/) |
| [awgym](https://github.com/Aitherium/awgym) | An ARC training gym — a game a world model can watch, and six roles that play through it | [docs](https://aitherium.github.io/awgym/) |
| [awpredict](https://github.com/Aitherium/awpredict) | Predict what your environment does next, and how surprised you were | [docs](https://aitherium.github.io/awpredict/) |
| [awevolve](https://github.com/Aitherium/awevolve) | Point an agent at a file and a command that scores it, and let it improve | [docs](https://aitherium.github.io/awevolve/) |
| [awsh](https://github.com/Aitherium/awsh) | Your terminal answers you -- type a question where a command would go | [docs](https://aitherium.github.io/awsh/) |
| [awmine](https://github.com/Aitherium/awmine) | Mine what your agents did -- outcomes, lessons and procedures out of the transcripts they left behind | [docs](https://aitherium.github.io/awmine/) |
| [awrise](https://github.com/Aitherium/awrise) | Wake an agent on a schedule, let it do one thing, and put it back to sleep | [docs](https://aitherium.github.io/awrise/) |
| **awkno** _(you are here)_ | The man page for the Aither World — every brick, stack and law, offline | [docs](https://aitherium.github.io/awkno/) |
| [awwall](https://github.com/Aitherium/awwall) | Say what a workload may reach, and watch everything else fail closed | [docs](https://aitherium.github.io/awwall/) |
| [awrouter](https://github.com/Aitherium/awrouter) | OpenRouter for your own fleet: pick a model backend by cost/latency/ capability, fail over, fit the context window, stream. Standalone, OpenAI-compatible, no Aither-specifics required to be valuable | [docs](https://aitherium.github.io/awrouter/) |
| [awembed](https://github.com/Aitherium/awembed) | Train an embedding model that knows your corpus, and prove it beats the big one | [docs](https://aitherium.github.io/awembed/) |
| [awtax](https://github.com/Aitherium/awtax) | Turn any tax PDF -- returns, W-2, 1099, statements, even scans -- into structured data you can check | [docs](https://aitherium.github.io/awtax/) |
| [awflow](https://github.com/Aitherium/awflow) | A deterministic workflow runtime — chain agent calls with journal replay and budget control | [docs](https://aitherium.github.io/awflow/) |
| [awsettings](https://github.com/Aitherium/awsettings) | Your agent's permissions and config, following you to the next machine | [docs](https://aitherium.github.io/awsettings/) |
| [awavatar](https://github.com/Aitherium/awavatar) | One character spec in, a rigged, animated, multi-style avatar pack out | [docs](https://aitherium.github.io/awavatar/) |

**Built on** [REA (Reverse Engineer Anything)](https://github.com/morluto/rea) · [llama.cpp](https://github.com/ggml-org/llama.cpp) · [vLLM](https://github.com/vllm-project/vllm) · [ComfyUI](https://github.com/comfyanonymous/ComfyUI) · [CentOS Stream](https://www.centos.org/centos-stream/) · [Podman](https://github.com/containers/podman) · [Docker](https://github.com/moby/moby) · [LanceDB](https://github.com/lancedb/lancedb) · [WireGuard](https://www.wireguard.com/) · [FFmpeg](https://ffmpeg.org/) · [Blender + Rigify](https://www.blender.org/) · [headroom](https://github.com/headroomlabs-ai/headroom) · [SANA](https://github.com/NVlabs/Sana) · [Hunyuan3D](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) · [repowise](https://github.com/repowise-dev/repowise) · [Playwright](https://github.com/microsoft/playwright) · [Chromium](https://www.chromium.org/) · [Next.js](https://github.com/vercel/next.js) · [React](https://github.com/facebook/react) · [PhotoCraft](https://github.com/storytold/photocraft).

<div id="aither-constellation" data-self="awkno"></div>
<script src="aither-constellation.js"></script>

<!-- aither-ecosystem:end -->
