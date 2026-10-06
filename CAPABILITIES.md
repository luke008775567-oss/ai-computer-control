# 100 AI Computer Assistant Capabilities

This roadmap expands the MCP server into a practical personal computer agent. Capabilities are grouped by purpose and should remain individually permission-gated where they can change data, communicate externally, spend money, or expose secrets.

## 1. Screen understanding
1. Screenshot the full display
2. Screenshot a selected region
3. Detect visible text with OCR
4. Find text on screen
5. Detect buttons
6. Detect links
7. Detect input fields
8. Detect menus
9. Detect dialogs
10. Describe the current screen

## 2. Mouse and keyboard
11. Move the pointer
12. Click
13. Double-click
14. Right-click
15. Middle-click
16. Drag and drop
17. Scroll
18. Type text
19. Press a key
20. Send keyboard shortcuts

## 3. Applications
21. Open an application
22. Quit an application
23. Focus an application
24. List running applications
25. Get the frontmost application
26. Hide an application
27. Minimize a window
28. Restore a window
29. Close a window
30. Switch between applications

## 4. Window management
31. List windows
32. Get window bounds
33. Move a window
34. Resize a window
35. Maximize a window
36. Tile windows
37. Arrange windows by workspace
38. Move a window between displays
39. Detect the active display
40. List connected displays

## 5. Browser automation
41. Open a URL
42. Create a browser tab
43. Close a browser tab
44. Switch browser tabs
45. Read page text
46. Find text on a webpage
47. Click webpage elements
48. Fill web forms
49. Download a file
50. Save a webpage as PDF

## 6. Files and folders
51. List files
52. Search for files
53. Create a folder
54. Rename a file
55. Move a file
56. Copy a file
57. Delete a file with confirmation
58. Read a text file
59. Write a text file
60. Inspect file metadata

## 7. Documents and data
61. Extract text from PDFs
62. Summarize PDFs
63. Extract tables from documents
64. Read DOCX files
65. Create DOCX files
66. Create spreadsheets
67. Read spreadsheets
68. Analyze CSV files
69. Convert common document formats
70. Generate reports

## 8. Communication
71. Draft an email
72. Search email
73. Summarize an email thread
74. Draft a reply
75. Create a calendar event
76. Find calendar availability
77. Draft a message
78. Summarize notifications
79. Prepare a meeting agenda
80. Prepare meeting notes

## 9. Personal productivity
81. Create a task
82. List tasks
83. Mark a task complete
84. Set a reminder
85. Create recurring reminders
86. Build a daily plan
87. Build a weekly plan
88. Track a multi-step workflow
89. Maintain a task state
90. Recover an interrupted workflow

## 10. Agent intelligence and safety
91. Maintain short-term task context
92. Produce a plan before acting
93. Ask for confirmation before risky actions
94. Require confirmation before external communication
95. Require confirmation before deleting data
96. Require confirmation before purchases
97. Keep an action audit log
98. Provide a dry-run mode
99. Provide an emergency stop
100. Report exactly what actions were taken

## Recommended implementation order

### Phase 1 — computer vision
OCR, screen regions, element detection, screen descriptions.

### Phase 2 — browser agent
Use Playwright for structured browser interaction instead of relying only on mouse coordinates.

### Phase 3 — files and documents
Safe filesystem tools plus document/PDF/spreadsheet processing.

### Phase 4 — productivity integrations
Email, calendar, tasks, and messaging through explicit connectors.

### Phase 5 — autonomous workflows
Planning, state, retries, verification, audit logs, and approval checkpoints.

## Security rule

The agent should never receive unrestricted shell execution, unrestricted filesystem access, silent credential extraction, or silent external communication. Sensitive operations should have explicit scopes and confirmation requirements.
