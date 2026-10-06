Session: `specification-foundation` — post-move repair
Session kind: repair. No canon is authored, no claim is filed, no criterion is written. Commit this prompt to `meta/sessions/` as the first act of the session, before anything else, per `CG-rule-06`. Session-neutral commit identity: `Claude <noreply@anthropic.com>`.
Repository: `mindovermachine-dev/specification-foundation`, default branch now `main`.
Standing rules

* You propose; Emil ratifies. Gates hold until an explicit ratification message.
* Three-register discipline in every gate output: rulings in force, `[PROPOSED]`, `[OPEN]`, kept distinct.
* British spelling throughout.
* Supersession never rewrites. Errors are corrected by appended note, never by amendment or force-push. A wrong value stays visible with the correction beside it.
* Report defects honestly, including in your own earlier output in this session.
* Name the weakest point in each proposal rather than leaving it for a reader to find.
* File arrived inputs with their sha256 before using them.

What happened, and why this session exists
The repository moved from the `Hafeok` account to the `mindovermachine-dev` organisation, as did `actor-indexed-determination`, `decision-driven-design` and (presumably) `canon-governance`. The move left references behind. The seed branch has since been renamed `main`.
Nothing about the move changes any determination. Everything in this session is reference hygiene and provenance, and the discipline is that a repair must not quietly become a revision.
Explicit prohibitions
You must not, in this session:

* author or amend any canon artefact under `canon/`, beyond what G-2 rules about references;
* write the conformance criterion, discrimination pairs, or anything about a binding;
* create any `SF-` claim record;
* advance the `canon-governance` pin — `CG-R-10` says a citation records what was read and complied with, not what is current, and going stale is its correct behaviour. A repository rename is not a change of what was read. If the pin's location needs restating, that is G-3's question and it is not the same act as advancing the ref;
* rewrite the README. Repair references and statements of fact about location; leave the argument alone.

G-1 — survey, before any edit
Report, with paths and line references:

1. Every reference to a `Hafeok/` URL or path, in every file including `canon/`, `evidence/`, `meta/`, `terms/`, `scripts/`, workflows, `CITATION.cff` and the licence files. Separate them into three classes, because they do not repair the same way:
   * live pointers — links a reader follows to find something now;
   * provenance — statements about where something was read, filed from, or cited at a moment in time. These are historical facts and must not be updated;
   * identifiers — anything where the string is a name rather than an address.
2. The branch and default state as found. Confirm `main` is the default and report whether any other branch exists, whether the old branch name still resolves, and whether any file or workflow refers to the former branch name.
3. Whether CI passes at `main` as it stands. Run the three validators and report their output verbatim. A move can break a path.
4. `CITATION.cff` — whether its `repository-code` or equivalent field points at the old location, and whether the citation string itself is affected. The citation was fixed at seed and is cited downstream; changing it is a different act from fixing a URL, and this gate must say which is required.
5. Anything that asserts a fact about location that is now false — not only links. A sentence saying a repository "is held in `Hafeok/canon-governance`" is a false statement, not a stale link.

GATE 1 — hold on the survey. No edits before it is ratified.
G-2 — the repairs
On ratification, repair only what G-1 classified as live pointers and false statements of location.
The rule that governs the hard cases: a reference that says where to find something now is repaired; a reference that says what was read, when is left exactly as it is, and if it is now ambiguous, the repair is an appended note saying the location changed, never an edit to the original line.
Report the diff before committing, grouped by class.
GATE 2 — hold.
G-3 — the governance citation
Separate from G-2 because it is governed by `CG-R-10` and must not be swept in with ordinary links.
The README cites `canon-governance` at `ad6d1b0b861306561364cc8d3a3e554cfb92d90c`, and `meta/canon-governance-ref.yaml` records the same value, with a validator asserting the two match.
The commit is unchanged by a rename. What may be wrong is the location at which it is to be found. Propose — do not assume — whether that is:

* (a) no change: the pin is a commit identity and the reader can locate it;
* (b) an appended note recording that the repository moved, with the pin itself untouched;
* (c) a repair to the location string with the pin untouched, if the location is part of the recorded value rather than prose around it.

Report what `meta/canon-governance-ref.yaml` actually contains, and whether the validator compares a URL or only a ref. The answer decides which of the three is even available.
And confirm, before proposing: does `canon-governance` still exist, and at what path? If it moved too, say so; if it did not, that is itself a finding worth stating, because then the programme is split across two accounts.
GATE 3 — hold.
G-4 — close

* Three validators green, output recorded verbatim.
* CI green on the branch.
* A short session record under `meta/sessions/` stating what was repaired, what was deliberately left as provenance, and the G-3 ruling with its reasoning.
* One PR. Nothing merged by you.

GATE 4 — hold.
Carried, not touched here
State these in the closing record so the next session inherits them rather than rediscovering them:

* The conformance criterion does not exist. The README's "when it lands" is accurate. The next substantive session writes it.
* `specification-languages` does not exist, and the README says so correctly.
* The resolution condition has no falsifier, per ruling R-1, and the closure pre-registration filed under `evidence/` tests a different claim. The standing recommendation on the record is retire and replace, not rewrite — a pre-registration whose claim changed is not a pre-registration. That decision is Emil's and is not taken here.
* The conformance relation has no validator, by recorded design.

Standing note
The weakest point of this session, named in advance: the line between a stale pointer and a historical fact is a judgement, and getting it wrong in the permissive direction destroys provenance silently. When a reference is genuinely ambiguous, treat it as provenance, append a note, and report it at the gate rather than deciding quietly. An over-cautious repair leaves a reader one extra click from the truth; an over-eager one leaves the record saying something that was never read.
