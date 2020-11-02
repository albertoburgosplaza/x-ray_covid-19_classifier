from pathlib import Path

DATA_PATH = Path("/workspaces/xrayc19/data")
POSITIVE_DATA_PATH = DATA_PATH / "positive"
POSITIVE_METADATA_PATH = POSITIVE_DATA_PATH / "bimcv_covid19_posi_head_iter1"
POSITIVE_DIAGNOSTIC_TESTS_PATH = (
    POSITIVE_METADATA_PATH / "derivatives" / "EHR" / "sil_reg_covid.tsv"
)
POSITIVE_RADIOLOGICAL_REPORTS_PATH = (
    POSITIVE_METADATA_PATH / "derivatives" / "labels" / "labels_covid19_posi.tsv"
)
POSITIVE_CUI_HIERARCHY_PATH = (
    POSITIVE_METADATA_PATH
    / "derivatives"
    / "labels"
    / "tree_term_CUI_counts_image_covid_posi.csv"
)
POSITIVE_PARTITIONS_PATH = POSITIVE_METADATA_PATH / "derivatives" / "partitions.tsv"
POSITIVE_PARTICIPANTS_PATH = POSITIVE_DATA_PATH / "participants.tsv"
