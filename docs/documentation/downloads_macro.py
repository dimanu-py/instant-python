import requests

def define_env(env):
	@env.macro
	def download_data(package: str):
		response = requests.get(f"https://pypistats.org/api/packages/{package}/overall?mirrors=false")
		return response.json()["data"]