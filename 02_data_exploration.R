library(summarizeNHTS)
download_nhts_data("2017", exdir="~/")
dataset <- read_data("2017", csv_path="~/")
statistic <- summarize_data(
    data = dataset,
    agg = "household_count",
    by = c("HHSIZE","HHVEHCNT")
)
make_chart(statistic)

# ERROR: dependencies ‘ggiraph’, ‘rgdal’ are not available for package ‘summarizeNHTS’
