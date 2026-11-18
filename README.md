# final-check

Τελικός έλεγχος μιας ολοκληρωμένης εργασίας (.docx) πριν την παράδοση, με μία εντολή στο Claude Code:

```
/final-check "C:\path\to\report.docx"
```

Βγάζει ένα HTML με δύο καρτέλες:

1. **Ανάγνωση κειμένου**: το Claude διαβάζει παράγραφο-παράγραφο και λέει human / AI / uncertain με αποδείξεις και εύρος ποσοστού (Mode B, δεν στέλνει τίποτα πουθενά).
2. **Μεταδεδομένα αρχείου**: τι σημάδια προέλευσης έχει το .docx (π.χ. `python-docx` ως συντάκτης, customXml) και ένα καθαρισμένο αντίγραφο `*.cleaned.docx`. Το πρωτότυπο δεν αλλάζει ποτέ.

> Ο έλεγχος δεν αποδεικνύει ότι η εργασία είναι «human» και δεν προβλέπει Turnitin/GPTZero. Έλεγξε και τους κανόνες του μαθήματος για δήλωση χρήσης AI.

## Τι χρειάζεσαι

- Windows, [Claude Code](https://claude.com/claude-code), Python 3, Git
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (ανοιχτό όταν τρέχεις τον έλεγχο)
- Το skill `ai-detector-check` του Claude (για την καρτέλα κειμένου). Χωρίς αυτό δουλεύει μόνο ο έλεγχος μεταδεδομένων.

## Εγκατάσταση

```powershell
git clone <URL αυτού του repo> final-check
cd final-check
powershell -ExecutionPolicy Bypass -File install.ps1
```

Το `install.ps1` αντιγράφει το skill στο `~\.claude\skills\final-check`, κλωνοποιεί δίπλα το [watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) (MIT, δεν περιλαμβάνεται εδώ) και ορίζει τις μεταβλητές `FINAL_CHECK_DIR` και `WATERMARKS_REMOVER_DIR`. Κλείσε και ξανάνοιξε το Claude Code μετά.

Την πρώτη φορά το Docker χτίζει την υπηρεσία (αργεί λίγα λεπτά). Μετά ξεκινά αυτόματα από το `meta_check.py`.

## Αρχεία

| Αρχείο | Τι κάνει |
|---|---|
| `skill/SKILL.md` | Η εντολή `/final-check` για το Claude Code |
| `meta_check.py` | Στέλνει το αρχείο στην τοπική υπηρεσία (127.0.0.1:8765), κάνει inspect + clean σε αντίγραφο, γράφει `cleaning-visual.html` |
| `combine.py` | Ενώνει τα δύο reports σε ένα HTML με καρτέλες |

## Άδεια

MIT. Το watermarks-remover έχει τη δική του MIT άδεια από τον δημιουργό του.
