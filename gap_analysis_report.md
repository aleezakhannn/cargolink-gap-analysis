# CargoLink ISO 27001 Gap Analysis Report

This report compares CargoLink's current controls against ISO 27001:2022 Annex A. All data comes from the local lab environment (sample data only).

## Summary

- Controls reviewed: 15
- Implemented: 3
- Gaps found (Partial or Missing): 12
- High priority gaps: 5

## Control Status

| Control ID | Control Title | Status |
|---|---|---|
| A.5.9 | Inventory of information and other associated assets | Implemented |
| A.5.15 | Access control | Partial |
| A.5.24 | Information security incident management planning | Missing |
| A.5.30 | ICT readiness for business continuity | Missing |
| A.6.3 | Information security awareness and training | Missing |
| A.7.4 | Physical security monitoring | Implemented |
| A.7.10 | Storage media | Partial |
| A.8.2 | Privileged access rights | Partial |
| A.8.5 | Secure authentication | Missing |
| A.8.7 | Protection against malware | Implemented |
| A.8.8 | Management of technical vulnerabilities | Missing |
| A.8.13 | Information backup | Partial |
| A.8.15 | Logging | Missing |
| A.8.20 | Networks security | Partial |
| A.8.24 | Use of cryptography | Missing |

## Identified Gaps

| # | Control ID | Control Title | Status | Asset | Sensitivity | Priority | Current State |
|---|---|---|---|---|---|---|---|
| 1 | A.5.24 | Information security incident management planning | Missing | Fleet Tracking Server | High | High | No written incident response plan |
| 2 | A.5.30 | ICT readiness for business continuity | Missing | Fleet Tracking Server | High | High | No tested recovery plan for the fleet tracking server |
| 3 | A.8.8 | Management of technical vulnerabilities | Missing | Fleet Tracking Server | High | High | No patching schedule for servers |
| 4 | A.8.15 | Logging | Missing | Cargo Manifest Database | High | High | No activity logs on the cargo manifest database |
| 5 | A.8.24 | Use of cryptography | Missing | Fleet Tracking Server | High | High | Fleet tracking data not encrypted at rest or in transit |
| 6 | A.7.10 | Storage media | Partial | Backup Storage Drive | High | Medium | Backup drive exists but is not encrypted or locked away |
| 7 | A.6.3 | Information security awareness and training | Missing | Dispatch Terminal 1 | Medium | Medium | No security training for dispatch or warehouse staff |
| 8 | A.5.15 | Access control | Partial | Cargo Manifest Database | High | Medium | Owners assigned but no documented access rules for the manifest database |
| 9 | A.8.13 | Information backup | Partial | Backup Storage Drive | High | Medium | Backup drive exists but restores are never tested |
| 10 | A.8.5 | Secure authentication | Missing | Dispatch Terminal 1 | Medium | Medium | No multi-factor authentication on dispatch terminals |
| 11 | A.8.2 | Privileged access rights | Partial | Admin Workstation | Medium | Low | Admin workstation in use but admin accounts may be shared |
| 12 | A.8.20 | Networks security | Partial | Office Wi-Fi Router | Medium | Low | Single office router with no network segmentation |

## Evidence

Screenshots are in the `evidence` folder:

- `evidence/script-output.png` - script run showing gaps found
- `evidence/tests-passed.png` - unit tests passing
