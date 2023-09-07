from flask import Flask, request, render_template, url_for, redirect
import sqlite3

app = Flask(__name__, static_folder='.', static_url_path='')

tasks = []


#データベースにつなぐ関数
#データベースを取得
def get_db():
	db = sqlite3.connect('memo.db')
	db.row_factory = sqlite3.Row
	return db

def init_db():
	with app.app_context():
		try:
			db = get_db()
		finally:
			db.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
	#データベースにつなぐ
	try:
		db = get_db()
		# task_id = int(request.form['task_id'])
		with db:
			tasks = db.execute('SELECT * FROM task').fetchall()
			categories = db.execute('SELECT * FROM category').fetchall()
			templates = db.execute('SELECT * FROM template').fetchall()
			# gifts = db.execute('SELECT * FROM gift').fetchall()
			
			if request.method == 'POST':
				
				task = request.form['task']
				category_id = int(request.form['category_id'])
				# btntemp = request.form['btntemp']
				# print('category_id:'+category_id)
				# tasks.append(task)
				with db:
					db.execute('INSERT INTO task (task_name,category_id) VALUES (?,?)', (task,category_id,))
					# db.execute('INSERT INTO task (task_name) VALUES(?)', (btntemp,))
			#データベースからtaskデータを取得
				return redirect('/')

			

			return render_template('index.html', tasks=tasks, categories=categories, templates=templates, )
			# ↑二つの配列(tasksとcategoriesを送る)
	finally:
		db.close()
	


@app.route('/finish', methods=['POST'])

def finish():

	try:
		db = get_db()
		task_id = int(request.form['task_id'])
	
		with db:
			db.execute('DELETE FROM task WHERE id = ?', (task_id,))
	# del tasks [task_id]
		return redirect('/')

	finally:
		db.close()


@app.route('/edit', methods=['POST'])
def edit():

	# del tasks[task_id]
	try:
		db = get_db()
		
		with db:
			task_id = int(request.form['task_id'])
			task_name = request.form['task_name']
			db.execute('UPDATE task SET task_name = ? WHERE id = ?', (task_name, task_id,))
		return redirect('/')

	
		
	finally:
		db.close()

templates = []		

@app.route('/temp', methods=['GET', 'POST'])
def temp():
	try:
		db = get_db()
		# template_id = int(request.form['template_id'])
		with db:
			templates = db.execute('SELECT * FROM template').fetchall()

			if request.method == 'POST':
				
				template = request.form['template']
				
			
				with db:
				
					db.execute('INSERT INTO template (template_name) VALUES(?)', (template, ))
					
				return redirect('/')	
			return render_template('index.html', templates=templates)
	finally:
		db.close()

# @app.route('/button', methods=['GET', 'POST'])	
# def button():
# 	try:
# 		db = get_db()
# 		with db:
# 			tasks = db.execute('SELECT * FROM task').fetchall()
			
# 			if request.method == 'POST':
# 				task = request.form['task']
# 				gift = request.form['gift']
				
# 				with db:
					
# 					db.execute('INSERT INTO gift (gift_name) VALUES(?)', (gift,))
# 					db.execute('UPDATE task SET gift_name = ? WHERE id = ?', (gift_name, gift_id,))
# 				return redirect('/')	
# 			return render_template('index.html', tasks=tasks)
		
# 	finally:
# 		db.close()	

@app.route('/finish2', methods=['POST'])
def finish2():
	try:
		db = get_db()
		template_id = int(request.form['template_id'])
	
		with db:
			db.execute('DELETE FROM template WHERE template_id = ?', (template_id,))
	
		return redirect('/')

	finally:
		db.close()	
			
	
# @app.route('/btntemp', methods=['POST'])
# def btntemp():
# 	try:
# 		db = get_db()
# 		template_id = int(request.form['template_id'])
# 		with db:
				
# 			# tasks = db.execute('SELECT * FROM task').fetchall()
# 			# if request.method == 'POST':
# 				return redirect('/')
# 			return render_template('index.html', tasks=tasks)
# 	finally:
# 		db.close()		



		


# 	return redirect('/')

# @app.route('/complete', methods=['POST'])

# def complete():
# 	task = 'complete_id'
# 	complete_id = int(request.form['complete_id'])

	
	


#  	# return redirect('/')
# 	return render_template('index.html')


#↓編集のSQLコード
# UPDATE task SET task_name = ? WHERE id = ?