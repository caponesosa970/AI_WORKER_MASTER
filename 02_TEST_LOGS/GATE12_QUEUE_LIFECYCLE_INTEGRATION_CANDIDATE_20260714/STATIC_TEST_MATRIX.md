# Static Test Matrix

Independent semantic validator: PASS

Cases: 57

| Case | Result |
| --- | --- |
| 01. invalid task199 mode | PASS |
| 02. controlled without latch | PASS |
| 03. launcher not armed | PASS |
| 04. launcher consumes authorization | PASS |
| 05. launcher calls task199 once | PASS |
| 06. production worker off | PASS |
| 07. controlled worker off | PASS |
| 08. controlled safe mode on | PASS |
| 09. production busy | PASS |
| 10. controlled busy | PASS |
| 11. router bad token | PASS |
| 12. send lock | PASS |
| 13. confirmation lock | PASS |
| 14. archive lock | PASS |
| 15. processing lock | PASS |
| 16. deadarchive lock | PASS |
| 17. compactor lock | PASS |
| 18. first read retry succeeds | PASS |
| 19. both reads fail | PASS |
| 20. parallel array mismatch | PASS |
| 21. invalid pending row | PASS |
| 22. invalid pending id | PASS |
| 23. one awaiting | PASS |
| 24. multiple awaiting | PASS |
| 25. awaiting plus danger | PASS |
| 26. sending | PASS |
| 27. send outcome unknown review | PASS |
| 28. post send status update failed | PASS |
| 29. hold pre send failed | PASS |
| 30. one done | PASS |
| 31. multiple done lowest | PASS |
| 32. awaiting plus done | PASS |
| 33. clear plus ready | PASS |
| 34. clear no ready | PASS |
| 35. confirm success no archive | PASS |
| 36. confirm failure no fallback | PASS |
| 37. archive success no process send | PASS |
| 38. archive failure no send | PASS |
| 39. send no same cycle confirm | PASS |
| 40. controlled no process | PASS |
| 41. controlled no maintenance | PASS |
| 42. controlled no recursion | PASS |
| 43. production handled skips process send | PASS |
| 44. production blocked skips process send | PASS |
| 45. production clear retains process | PASS |
| 46. one task71 node | PASS |
| 47. one task227 node | PASS |
| 48. one task225 node | PASS |
| 49. one task226 node | PASS |
| 50. no broad archive call | PASS |
| 51. no task75 call | PASS |
| 52. one module maximum | PASS |
| 53. owned busy release once | PASS |
| 54. no unowned busy release | PASS |
| 55. profiles disabled | PASS |
| 56. protected task preservation | PASS |
| 57. no private tracked | PASS |

Failed structural checks: 0.

Failed matrix cases: 0.

This matrix is static model evidence. It does not prove Tasker rendering or phone behavior.
