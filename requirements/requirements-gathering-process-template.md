# Requirements Gathering (Shape Up) — Simple

- Owner: 
- Date: 
- Appetite (time/people): 
- Links (pitch/bet, metrics): 

## 1) Problem & Outcome

- Problem to solve (one paragraph): 
- Users/personas impacted: 
- Success metrics (observable outcomes): 

## 2) Scope

- In scope: 
- Out of scope (no-gos): 

## 3) Approach (Fat-Marker)

- One-paragraph concept: 
- Flow sketch/breadboard link: 
- Key states and transitions:
  - State A → State B
  - Error/empty/loading

## 4) Rules & Constraints (Just Enough)

- Eligibility/validation rules: 
- Performance/latency expectations: 
- Accessibility considerations: 
- Data/privacy (e.g., LGPD/GDPR, PII): 

## 5) Risks & Rabbit Holes

- Top risks (impact × uncertainty): 
- Things to avoid: 
- Assumptions to validate: 

## 6) Dependencies

- Systems/APIs/teams: 
- Sequencing or external timelines: 

## 7) Test Scenarios (Outline)

```gherkin
Feature: <Feature name>

  Background:
    Given <preconditions>

  Scenario: Happy path
    When <user action>
    Then <expected outcome>

  Scenario: Validation error
    When <invalid input>
    Then <error message>

  Scenario: Dependency failure
    When <dependency behavior>
    Then <graceful handling>
```

## 8) Decision & Handoff

- Decision (bet / not yet / rejected): 
- Handoff checklist:
  - [ ] Appetite/timebox agreed
  - [ ] Sketches/flows linked
  - [ ] Rules captured at just-enough detail
  - [ ] Test scenarios outlined
  - [ ] Single owner named

## 9) Decision Log (optional)

- YYYY-MM-DD — Decision — Why — Owner
