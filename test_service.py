import requests
import logging

logging.basicConfig(
    filename="test_service.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_recommendations(test_case, recs_offline, recs_online, recs_blended):
    """Логирует результаты рекомендаций."""
    logging.info(f"=== {test_case} ===")
    logging.info(f"Оффлайн рекомендация: {recs_offline}")
    logging.info(f"Онлайн рекомендация: {recs_online}")
    logging.info(f"Смешанная рекомендация: {recs_blended}")
    logging.info("=====================")

recommendations_url = "http://127.0.0.1:8000"
features_store_url = "http://127.0.0.1:8010"
events_store_url = "http://127.0.0.1:8020"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

### Test 1: Юзер без персональных рекомендаций
user_id_no_personal = 123456789
params = {"user_id": user_id_no_personal, 'k': 10}
resp_offline = requests.post(recommendations_url + "/recommendations_offline", headers=headers, params=params)
resp_online = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
resp_blended = requests.post(recommendations_url + "/recommendations", headers=headers, params=params)

recs_offline = resp_offline.json()["recs"]
recs_online = resp_online.json()["recs"]
recs_blended = resp_blended.json()["recs"]

log_recommendations("Тест 1: Юзер без персональных рекомендаций", recs_offline, recs_online, recs_blended)

### Test 2: Юзер с персональными рекомендациями, но без онлайн-истории
user_id = 711030
params = {"user_id": user_id, 'k': 10}
resp_offline = requests.post(recommendations_url + "/recommendations_offline", headers=headers, params=params)
resp_online = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
resp_blended = requests.post(recommendations_url + "/recommendations", headers=headers, params=params)

recs_offline = resp_offline.json()["recs"]
recs_online = resp_online.json()["recs"]
recs_blended = resp_blended.json()["recs"]

log_recommendations("Тест 2: Юзер с персональными рекомендациями, но без онлайн-истории", recs_offline, recs_online, recs_blended)

### Test 3: Юзер с персональными рекомендациями и онлайн-историей
user_id = 711033
event_item_ids =  [37538957, 27965, 545860, 21738305]

for event_item_id in event_item_ids:
    resp = requests.post(events_store_url + "/put", 
                         headers=headers, 
                         params={"user_id": user_id, "item_id": event_item_id})

params = {"user_id": user_id, 'k': 10}
resp_offline = requests.post(recommendations_url + "/recommendations_offline", headers=headers, params=params)
resp_online = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
resp_blended = requests.post(recommendations_url + "/recommendations", headers=headers, params=params)

recs_offline = resp_offline.json()["recs"]
recs_online = resp_online.json()["recs"]
recs_blended = resp_blended.json()["recs"]

log_recommendations("Тест 3: Юзер с персональными рекомендациями и онлайн-историей", recs_offline, recs_online, recs_blended)