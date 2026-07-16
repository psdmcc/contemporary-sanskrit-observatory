# Ontology

The Contemporary Sanskrit Observatory represents contemporary Sanskrit communication as a network of related entities.

The ontology provides the conceptual model upon which all collections, metadata, computational analyses, and publications are built.

## Core Entities

### Collection

A curated group of communicative events assembled for a common scholarly purpose.

Examples:

- Broadcast News
- Conversation
- Sports Commentary

---

### Institution

An organisation responsible for creating, hosting, publishing, funding, or preserving communicative events.

Examples:

- Doordarshan
- All India Radio
- Samskrita Bharati
- Central Sanskrit University

---

### Person

An identifiable participant in one or more communicative events.

Roles are defined by participation in events rather than fixed globally.

Examples include:

- presenter
- interviewer
- interviewee
- commentator
- author
- editor
- translator

---

### Event

A communicative act occurring at a specific time and place.

Examples include:

- news broadcast
- lecture
- interview
- sports commentary
- conversation
- theatrical performance

Events are the primary observational units of the Observatory.

---

### Artifact

A physical or digital object produced by an event.

Examples:

- YouTube video
- audio recording
- printed book
- PDF
- web page

One event may generate multiple artifacts.

---

### Document

A machine-readable representation derived from an artifact.

Examples:

- transcript
- OCR text
- subtitle file
- TEI document
- translation

Documents are the primary computational units.

---

### Observation

A reproducible measurement generated from one or more documents.

Examples:

- token count
- type-token ratio
- compound density
- lexical diversity
- topic distribution

---

### Knowledge Object

A durable scholarly product derived from observations.

Examples:

- register profile
- institution profile
- lexical profile
- comparative analysis
- publication
- visualization

---

## Entity Relationships

```
Collection
    │
    ▼
Event
    │
    ▼
Artifact
    │
    ▼
Document
    │
    ▼
Observation
    │
    ▼
Knowledge Object

Institution ───────────────┐
                            │
Person ─────────────────────┘
           participates in Events
```

The ontology is intentionally minimal.

Additional entities should only be introduced when they cannot be represented through existing relationships.
