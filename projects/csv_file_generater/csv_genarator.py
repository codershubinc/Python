from util import gen_data , fetch_data

url = "https://openapihub.vercel.app/v1.0/contry/CA"
data = fetch_data(url)



gen_data(
    100,
    data
)