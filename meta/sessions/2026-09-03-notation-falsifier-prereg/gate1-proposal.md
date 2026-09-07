# Gate 1 proposal — the act and its determination set

**Status: `[PROPOSED]`.** Nothing here is ratified. Per `CG-R-21` the determination set is
proposed as **provisional**: it closes against the frame after Gate 2, closure adds and never
revises, and the closed set is what Gate 3 fixes. Per `CG-R-27` the act is not `PlaceOrder`, and
§1 says why the rule could not have chosen it.

Neither arm is authored here. The set is content — an inventory in the foundation's construct
vocabulary, not records and not prose specification. Whoever writes arm R and whoever writes
arm P each receive this inventory and nothing of the other's work.

---

## 1. The act

### 1.1 Selection rule

Three steps. A third party applying them to the arrived bundle reaches the same slice.

1. **Draw from the event models the binding ships** (`ordering`, `fulfilment`). Arm R must
   address a slice the act vocabulary names, or the binding's address-validity check cannot run
   on it; and inventing an event model would be authoring the notation's base, which is not this
   session's to do.
2. **Exclude every slice that is the address of any shipped determination.** That is
   `CG-R-27` generalised from `PlaceOrder` to everything the example already speaks for:
   `PlaceOrder` (DSC-0001, -0002, -0003, -0005), `OrderSummary` (DSC-0004), `ConfirmOrder`
   (DSC-0006), `ScheduleShipment` (DSC-0101), `ShipmentBoard` (DSC-0102). Remaining:
   `AddToCart` (command), `Cart` (read-model), `EmptyCart` (command).
3. **Of the remaining, take the first in the order the event model lists them.** Listing order
   is the least discretionary tiebreak available: it is reproducible, and it does not select on
   the slice's decision content — which is what a session fluent in the domain would otherwise
   be tempted to do, and would be selecting for the outcome.

**Result: `command:AddToCart`, ordering context, act scale.**

Rules considered and not used, with what each yields, so the choice of rule is visible: *largest
combined ground and verdict set* yields `Cart` (three facts to two); *commands only, then first
listed* yields `AddToCart` as well; *richest decision content* would also land on `AddToCart` but
is a judgement, not a rule. Had step 3 yielded `Cart` or `EmptyCart` the session would have
proposed it; the rule was fixed before it was applied.

### 1.2 What performing the act is

The actor receives the specification in one arm's form, and the act's base — the slice, what it
reads and what it writes — and produces the implementation of the `AddToCart` command slice:
the handler that accepts the command, reads the `Cart`, and either rejects the command or emits
`ItemAddedToCart`. One turn; the output is what Gate 4's stage 1 reads. Language and everything
else about the actor are §6.5's, fixed at Gate 3. This is an act a model can plausibly attempt
end to end: it is one handler over one entity and one event.

**The base is delivered identically to both arms.** The event model is the act vocabulary, not
the notation under test. How it is delivered is a Gate 3 item, flagged now: the shipped model is
YAML, and handing YAML to arm P's actor beside a prose specification is a cue in the wrong
direction. Recommendation for Gate 3: a short prose statement of the slice, identical in both
arms, in place of the YAML.

### 1.3 The act's ground and verdict, from the event model

Fixed by the arrived input, not by this session.

| Position | Fact | Kind | Boundary |
|---|---|---|---|
| ground (read) | `Cart` | entity, produced by the `Cart` read-model slice | internal |
| verdict (write) | `ItemAddedToCart` | event, read by the `Cart` read-model slice | internal |

The act reads no `ActorIdentity`: the event model gives `AddToCart` no such ground, and the
binding's address-validity check would reject a determination declaring one. That fixes one
residual (AC-07) and it is a limit of the selection (§7): **no external ground and no terminal
verdict occur at this act**, so B-1 and B-2 are not exercised by the set.

### 1.4 Contamination at this act, stated

- Shipped determination DSC-0002 (payload typing, checked) **travels to all command slices**, so
  it nominally reaches `AddToCart`. The set does not carry it; nothing of its content is reused.
  The frame category it would settle is closed under `CG-R-21` like any other.
- The binding README paraphrases none of `AddToCart`'s content. The event model's comment on the
  `Cart` slice records that the projection was forced in by the resolution check; that is about
  the base, not about any determination here.
- The set's identifiers `AC-01` … `AC-11` are this session's, for the Gate 3 mapping table. Arm R
  uses `DSC-` identifiers of its author's choosing; arm P uses none. A cross-reference between
  determinations (AC-11 → AC-06) is content and is expressed in each arm's own way.

## 2. The determination set — content inventory

Vocabulary is the foundation's (`canon/specification-language-foundation.md` §2): **act**,
**ground requirement**, **determination**, **extent**, **allocation**, **acceptance relation**,
**coverage and residual**, **provenance**. Positions follow S-2: read position is ground, write
position is verdict. Every row is content both arms must carry; Gate 3's parity check is
item-by-item against these tables.

**Provenance values are content.** The workshop, the architecture decision and the session named
below are the fictional domain's, fixed as given; they are not claims about events in this
programme. Timestamps are likewise content.

**Convention basis** per `CG-R-22`: *conventional* — the resolution a competent actor would
default to; *counter-conventional* — one they would not, on one of two bases: **departs** (a
default exists and the determination contradicts it, named) or **specific** (no default produces
the value). Residuals carry no basis: there is no resolution to match.

### AC-01 — repeat adds make new lines

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | Adding a product the cart already holds creates a new line. Lines are never merged, and a later add never changes an existing line's quantity. |
| extent | slice-type: bound here · context: does not travel to `fulfilment` — fulfilment has no carts; a shipment line is formed from an order, not from a cart line · sector: silent |
| allocation | **pinned**; settled by `cart-workshop-2026-08-21: separate-lines` |
| ground / verdict | ground `Cart` (internal) · verdict `ItemAddedToCart` (internal) |
| provenance | build-time · `cart-workshop-2026-08-21` · 2026-08-21T09:10:00Z |
| basis | **counter-conventional, departs** — the default merges a repeat add into the existing line by incrementing its quantity |

### AC-02 — quantity bounds, no clamping

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | The command carries a quantity: an integer from 1 to 20 inclusive. A quantity outside that range rejects the command. It is never clamped to the nearest bound. |
| extent | slice-type: bound here · context: bound here · sector: silent |
| allocation | **pinned**; settled by `cart-workshop-2026-08-21: quantity-bounds` |
| ground / verdict | verdict `ItemAddedToCart` (internal) |
| provenance | build-time · `cart-workshop-2026-08-21` · 2026-08-21T09:20:00Z |
| basis | **counter-conventional, departs and specific** — the default accepts any positive integer or clamps; 20 is produced by no default |

### AC-03 — no catalogue at add

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | The command does not consult the product catalogue. Whether the product exists, is purchasable, or is priced is not checked when adding; the product identifier is recorded as supplied. Catalogue checks belong to `PlaceOrder`. |
| extent | slice-type: bound here · context: bound here · sector: silent |
| allocation | **pinned**; settled by `cart-workshop-2026-08-21: no-catalogue-at-add` |
| ground / verdict | ground `Cart` (internal); the catalogue is expressly not ground at this act |
| provenance | build-time · `cart-workshop-2026-08-21` · 2026-08-21T09:30:00Z |
| basis | **counter-conventional, departs** — the default validates the product against the catalogue at add time |

### AC-04 — line cap

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | A cart holds at most 50 lines. An add that would create a 51st line is rejected and the cart is unchanged. |
| extent | slice-type: bound here · context: bound here · sector: silent |
| allocation | **checked** |
| acceptance relation | predicate: *no `ItemAddedToCart` is emitted for a cart that already holds 50 lines* · closure: **logical only** — decidable from the `Cart` projection; no test in the arrangement runs it · tolerance: exact · ranges over: `ItemAddedToCart` |
| coverage and residual | covers: line-cap enforcement · does not cover: two adds racing the cap (both read 49 lines); unit totals (the cap counts lines, not units) · **proxy**: stands in for *a customer cannot assemble a cart too large to check out or fulfil*; known divergence: *the cap counts lines, not units — 50 lines at quantity 20 is 1,000 units and passes* |
| ground / verdict | ground `Cart` (internal) · verdict `ItemAddedToCart` (internal) |
| provenance | build-time · `cart-workshop-2026-08-21` · 2026-08-21T09:45:00Z |
| basis | **counter-conventional, departs and specific** — the default imposes no line cap; 50 is produced by no default |

### AC-05 — repeat delivery is absorbed

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | An add whose line identifier is already present in the cart is a repeat delivery of an earlier add. It succeeds, emits nothing, and changes nothing. |
| extent | slice-type: bound here · context: bound here · sector: silent |
| allocation | **checked** |
| acceptance relation | predicate: *for any `AddToCart` whose line identifier already appears in the cart, no `ItemAddedToCart` is emitted and the command reports success* · closure: **operational** — runnable by `integration-test:RepeatAddIsAbsorbed`; terminates · tolerance: exact · ranges over: `ItemAddedToCart` |
| coverage and residual | covers: repeat delivery of one add · does not cover: a repeat arriving before the projection reflects the first; a second, distinct add of the same product (a new line, per AC-01) |
| ground / verdict | ground `Cart` (internal) · verdict `ItemAddedToCart` (internal) |
| provenance | build-time · `cart-workshop-2026-08-21` · 2026-08-21T10:00:00Z |
| basis | **counter-conventional, departs** — the default rejects a duplicate as a conflict, or emits a second event |

### AC-06 — price capture, residual

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | Whether a line is priced at the moment of adding, from a price the caller supplies, or only when the order is placed, is not settled here. |
| extent | slice-type: bound here · context: bound here · sector: silent |
| allocation | **residual**; carried by a team; accountable principal: team `pricing` |
| ground / verdict | verdict `ItemAddedToCart` (internal) |
| provenance | build-time · `cart-workshop-2026-08-21` · 2026-08-21T10:15:00Z |
| basis | not applicable — residual |

### AC-07 — caller-to-cart binding, residual

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | The command names the customer whose cart receives the line. Whether the caller must be that customer, and what happens when it is not, is not settled here. |
| extent | slice-type: bound here · context: silent · sector: silent |
| allocation | **residual**; carried by a human; accountable principal: team `identity-and-access` |
| ground / verdict | none in the fact vocabulary — the act reads no `ActorIdentity` (§1.3) |
| provenance | build-time · `cart-workshop-2026-08-21` · 2026-08-21T10:20:00Z |
| basis | not applicable — residual |

### AC-08 — cart per customer, created by first add

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | A cart is identified by the customer identifier the command carries. No separate act creates a cart: the first add to a customer's cart brings it into existence, and an add for a customer with no cart succeeds. |
| extent | slice-type: bound here · context: bound here · sector: silent |
| allocation | **pinned**; settled by `cart-workshop-2026-08-21: cart-per-customer` |
| ground / verdict | ground `Cart` (internal) |
| provenance | build-time · `cart-workshop-2026-08-21` · 2026-08-21T10:30:00Z |
| basis | **conventional** — create-on-first-add keyed by customer is the default |

### AC-09 — rejections are named; travels

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale — reached by travel |
| determination | A rejected command reports the rejection with the name of the field or condition that caused it. Commands never fail silently and never partially succeed. |
| extent | slice-type: travels to all command slices — a pattern-level determination, collected by every command slice · context: travels to all contexts · sector: silent |
| allocation | **pinned**; settled by `arch-decision-14: named-rejections` |
| ground / verdict | none declared — a rejection is not a fact in the vocabulary |
| provenance | build-time · `arch-decision-14` · 2026-08-19T15:00:00Z |
| basis | **conventional** — a named rejection is the default |

### AC-10 — caller-supplied line identifier; act-time

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | The line identifier is supplied by the caller in the command, as a UUID. The handler does not generate identifiers. A command with no line identifier, or one that is not a UUID, is rejected. |
| extent | slice-type: bound here · context: bound here · sector: silent |
| allocation | **pinned**; settled by `session-ruling:2026-08-27-cart-projection` |
| ground / verdict | verdict `ItemAddedToCart` (internal) |
| provenance | **act-time** · `session:2026-08-27-implement-cart-projection` · 2026-08-27T16:40:00Z |
| basis | **counter-conventional, departs** — the default has the handler assign the identifier |

### AC-11 — event content

| Construct | Content |
|---|---|
| act | `command:AddToCart`, act scale |
| determination | `ItemAddedToCart` carries the customer identifier, the line identifier, the product identifier, the quantity, and the time the command was accepted. Whether it also carries a price is not settled here (AC-06). |
| extent | slice-type: bound here · context: does not travel to `fulfilment` — fulfilment never reads cart events · sector: silent |
| allocation | **pinned**; settled by `cart-workshop-2026-08-21: event-content` |
| ground / verdict | verdict `ItemAddedToCart` (internal) |
| provenance | build-time · `cart-workshop-2026-08-21` · 2026-08-21T10:40:00Z |
| basis | **conventional** — these are the fields a competent actor carries; the accepted-at timestamp is a defaultable choice |

## 3. What the set contains, summarised

| Property | Count | Which |
|---|---|---|
| determinations | 11 | AC-01 … AC-11 |
| pinned | 7 | AC-01, -02, -03, -08, -09, -10, -11 |
| checked | 2 | AC-04 (logical-only closure, with proxy), AC-05 (operational closure) |
| residual | 2 | AC-06 (team-carried), AC-07 (human-carried) |
| counter-conventional, **departs** basis | 6 | AC-01, -02, -03, -04, -05, -10 |
| of which also **specific** | 2 | AC-02 (20), AC-04 (50) |
| conventional | 3 | AC-08, -09, -11 |
| act-time provenance | 1 | AC-10 |
| extent states used | all four | bound here (throughout); travels to (AC-09, two axes); does not travel (AC-01, AC-11, with region and reason); silent (sector throughout; context in AC-07) |
| boundary kinds used | internal only | see §1.3 and §7 |
| constructs not exercised | — | external ground (B-1), terminal verdict (B-2), supersession, `asserted-none` coverage |

The prompt's minimums are met: at least one of each allocation class, and at least one declared
residual. `CG-R-22`'s requirement is met with six counter-conventional determinations; the
minimum subset size is Gate 3's to fix, and Gate 3 should consider fixing it on the *departs*
basis only, since *specific* is the weaker of the two (a match on a number is evidence of
retrieval; a match on a departure is evidence of retrieval against a pull).

## 4. Internal consistency, checked

- AC-01 (distinct line identifiers are distinct lines, same product or not) and AC-05 (the same
  line identifier is a repeat) partition the "same product again" case cleanly; AC-05's uncovered
  set says so.
- AC-10 (caller supplies the identifier) is what makes AC-05 decidable; AC-05 makes no sense
  with handler-assigned identifiers.
- AC-02 (quantity ≤ 20 per line) and AC-04 (≤ 50 lines) compose to AC-04's proxy divergence
  (1,000 units passes).
- AC-03 (no catalogue at add) and AC-06 (price residual) are coherent: with no catalogue read, a
  price at add time can only be caller-supplied, which is the alternative AC-06 leaves open.
- AC-08 (cart keyed by the customer identifier in the command) and AC-07 (caller binding
  residual) are coherent: the identifier is trusted as supplied because nothing here binds it.
- AC-11 names the fields and defers price to AC-06; AC-06 is the only residual AC-11 depends on.
- Every ground and verdict declared is one the event model gives `AddToCart`; the binding's
  address-validity check will accept arm R's positions if arm R follows the inventory.

**What arm R can and cannot be checked against.** Schema validity and address validity, yes.
The context-level resolution condition, only together with the shipped example's boundary
declarations (`ActorIdentity` external, `OrderConfirmed` terminal), which are not in this set and
belong to other acts. The executing session should run the resolution check over the union, not
over arm R alone, and say so.

## 5. Consequences for later gates

- **Closure (`CG-R-21`).** After Gate 2, every frame category the set neither disposes of nor
  declares is closed. Recommendation: closure adds **residual declarations only**. Adding new
  determinations once the frame is visible would let the determined partition, and the
  counter-conventional subset, be tuned to the denominator; a new determination at closure needs
  a stated reason and separate ratification.
- **Frame vocabulary and coverage vocabulary (Gate 2).** AC-04 and AC-05 name properties in
  their covers and uncovered sets. Gate 2 draws the list from the act type, not from this set; if
  a frame category coincides with one of those names, both arms carry it by parity and the
  leakage check passes as §8 words it.
- **Parity (Gate 3).** The inventory above is the parity list. Gate 3 enumerates it as a
  numbered checklist, one item per cell fragment, and the check is: every item present in R,
  every item present in P, no item present in one and absent from the other. The P author
  receives §2 and §1.3, never arm R.
- **Base delivery (Gate 3).** §1.2's recommendation: the slice stated in prose, identically, in
  both arms.
- **Rubric (Gate 4).** An explicit override — the output says the specification settles a
  category and resolves it otherwise — needs a cell; see §7.

## 6. Threats specific to this selection

- **Domain oddness.** Six of nine determined-partition determinations depart from convention.
  An actor may read the specification as mistaken and "correct" it. That scores inferred in both
  arms and is not a bias unless notation affects it (§7).
- **Thin act.** One ground, one verdict, both internal. Boundary categories in the frame will be
  disposed of trivially or closed as residual; the set exercises the notation's allocation,
  extent, acceptance and coverage constructs and not its boundary constructs.
- **Small frame.** Eleven determinations on one handler bound the determined partition at the
  low tens. Gate 3's detectable effect will be coarse. Stated here so Gate 3 does not discover it.

## 7. Weakest point of the selection

**Counter-conventional content tests compliance as well as retrieval, and notation may affect
compliance without affecting legibility.** `CG-R-22` makes a match evidence of retrieval; it also
makes a mismatch ambiguous between *did not retrieve* and *retrieved and overrode*. An explicit
override is distinguishable — stage 1 can mark "resolved contrary to a stated determination" —
and Gate 4 must give it a cell, because scoring it *inferred* is wrong (the actor retrieved) and
scoring it *determined* is wrong (the disposition is not the set's). A silent override is not
distinguishable from inference and scores inferred. If records read as more authoritative than
prose, R's override rate falls for a reason that is not legibility, and the primary measure moves
in the predicted direction on it. This is the price of `CG-R-22` and is not removable by choosing
determinations differently; it is reported per arm as the explicit-override count, which is the
only part of it that can be seen.

---

**Hold.** Gate 2 is not entered. Awaiting explicit ratification of Gate 1 as provisional, per
`CG-R-21`.
