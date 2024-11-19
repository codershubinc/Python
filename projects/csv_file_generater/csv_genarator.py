from util import gen_data , fetch_data

url = "https://openapihub.vercel.app/v1.0/contry/IN"
data = fetch_data(url)



gen_data(
    100000,
    data
)