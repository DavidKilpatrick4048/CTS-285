# M3 Product Owner Decision Record

## Scenario
StudyTrack release planning under constrained capacity.

## Round 1 — Capacity 13
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

**Why this release slice was defensible:**
ST-02 and ST-03 are included with ST-01 because they depend on task creation. ST-04 is included because accessible keyboard task entry is high value, ready to build and low effort.  This includes creating a task, marking it complete and recovering a missed task. This work fits capacity and directly supports the release goal without adding unnecessary features.

**One intentional deferral and why:**
I deferred ST-05, Weekly Progress Summary because while it is useful it is not required for the basic ability to plan study work and recover missed tasks.  It also depends on ST-01 and ST-02, so the planning and recovery items are higher priority right now.

## Complication
Capacity dropped from 13 to 10 points. Keyboard accessibility testing revealed that task entry cannot reliably be completed with keyboard navigation, so ST-04 became release-critical.

## Revised Release Slice — Capacity 10
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

### Removed after complication
- None

### Added after complication
- None

**What changed and why:**
Nothing. The original plan accounted for 10 effort points. ST-04 was already planned.  The new accessibility finding changed ST-04 from high value to required for release.

**Tradeoff accepted:**
I accepted deferring the weekly progress summary and other non-core features. This preserves the essential ability to create, complete, and recover study tasks while ensuring keyboard accessibility.

## Transfer to DataMan
Before finalizing your DataMan backlog, review whether any item is high value but not ready, depends on unresolved work, consumes disproportionate effort, or should move because it reduces risk or unlocks other work.
