# Kinetra Studios Prototype Reliability Gate v1

Before a Studios prototype is presented as decision support, it must declare: source/provenance, freshness if time-sensitive, action authority, human owner, rollback path, frozen test version, critical mismatch count and known limitations.

**Release rule:** critical mismatch > 0 => no external release.  
**Claim rule:** synthetic test pass never becomes a production accuracy or safety guarantee.

Reference rubric: `../public-proof/reliability-regression-v2/rubric.json`.
