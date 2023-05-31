from flask import Flask
from flask import render_template
from flask import request, jsonify, redirect
from search_res import search_res
import json

app = Flask(__name__)

# with open("./static/images/Areca Palm.jpg", 'rb') as f:
# 	image_bytes = f.read()
# 	print(get_prediction(image_bytes=image_bytes))


#HTML 렌더링
@app.route('/')
def home_html():
	plants_list = ["아레카야자","벤자민고무나무","클레로덴드럼","크로톤","팔손이","호야","네프롤레피스","파키라","나한송","드라세나 콤팩타","드라세나 드라코","드라세나 와네키","몬스테라","페페로미아","산세베리아","칼라데아 오르비폴리아","스킨답서스","필로덴드론 셀레움","스파티필름","스투키"]
	return render_template('index.html', plants = plants_list)

#쇼핑 검색 결과
@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == 'POST':
		req_text = request.form['search']
		result_res = search_res(req_text)
		item_len = result_res['display']
		return render_template('display.html', search=result_res['items'], item_len=item_len)
	return render_template('index.html')


	
#서버 실행
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug = True)
