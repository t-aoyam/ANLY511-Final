library(data.table)
library(stringr)

df <- fread(file = "kindle_reviews.csv")
df_s <- df[sample(nrow(df), 10000)]

df_s$helpful_a = numeric(10000)
for(i in 1:nrow(df_s)){
  temp <- str_split(str_remove_all(df_s[i,]$helpful, "[^a-zA-Z|0-9|,]"), ',', simplify = TRUE)
  if(as.integer(temp[,2]) != 0){
    df_s[i,]$helpful_a = as.numeric(temp[,1])/as.numeric(temp[,2])
  }
  else{
    df_s[i,]$helpful_a = NA
  }
}