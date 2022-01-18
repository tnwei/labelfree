# Download zip from NASA Prognostics Data Repo
wget https://ti.arc.nasa.gov/c/8/ -O SentientData.zip

# Unzip into `data/raw/`
mkdir data
unzip SentientData.zip "Sentient Data/*" -d data/
mv "data/Sentient Data" data/raw

# Remove raw zip file
rm SentientData.zip