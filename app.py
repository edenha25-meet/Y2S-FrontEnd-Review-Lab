from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return (
        "<html>"
        "<h1>Photo Gallery!</h1>"
        "<p>In this gallery there will be three types of photos</p>"
        "<div></div>"
        "<a href='/food'>Go to the first food photo</a>"
        "<div></div>"
        "<a href='/pet2'>Go to the second pet photo</a>"
        "<div></div>"
        "<a href='/space1'>Go to the first space photo</a>"
        "</html>"
    )

@app.route('/food')
def food1():
    return (
        "<html>"
        "<img src='https://twoplaidaprons.com/wp-content/uploads/2020/05/Chinese-pork-dumplings-picking-up-a-dumpling-with-chopsticks.jpg' width='400'>"
        "<div></div>"
        "<a href='/food2'>Go to the second food photo</a>"
        "<div></div>"
        "<a href='/home'>Go to the home page </a>"
        "</html>"
    )
@app.route ('/food2')
def food2():
    return('''
        <html>
        <img src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBnfTXs9DpaPffvPTpjsS2XrGmEqiS1PebKA&s' width= '400'>
        <div></div>
        <a href='/food3'>Go to the third food photo</a>
        <div></div>
        <a href='/food'>Go to the previous page</a>
        </html>

       ''' )
@app.route ('/food3')
def food3():
       return('''
        <html>
        <img src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbgi_Vi38CdsBx-YZZ30yr6VvheFhXCHgqNg&s' width= '400'>
        <div></div>
        <a href='/home'>Go to the home page</a>
        <div></div>
        <a href='/food2'>Go to the previous page </a>
        </html>

      '''  )
@app.route('/pet1')
def pet1():
    return( '''       
        <html>
        <img src = 'https://cdn1.byjus.com/wp-content/uploads/blog/2023/03/17131610/STIM_Happy-Baby-Elephant-Running-scaled.jpeg' width= '400'>
        <div></div>
        <a href='/pet2'>Go to second pet picture</a>
        </html>
       ''' )
@app.route('/pet2')
def pet2():
    return( '''
        <html>
        <img src = 'https://c02.purpledshub.com/uploads/sites/41/2021/03/Blobfish_Kerryn-Parkinson-hero-47ec84c.jpg' width= '400'>
        <div></div>
        <a href='/pet1'>Go to previous page</a>
        <div></div>
        <a href='/home'>Go to the home page</a>
        <div></div>
        <a href='/pet3'>Go to the third picture</a>
        </html>
        ''')
@app.route('/pet3')
def pet3():
    return('''
        <html>
        <img src = 'https://www.shutterstock.com/shutterstock/photos/2227972059/display_1500/stock-photo-cute-young-cobberdog-aka-labradoodle-dog-puppy-sitting-up-side-ways-looking-towards-camera-2227972059.jpg' width= '400'>
        <div></div>
        <a href='/pet2'>Go to previous page</a>
        <div></div>
        </html>
        ''')
@app.route('/space1')
def space1():
    return('''
        <html>
        <img src = 'https://encyclopedia.pub/media/common/202210/mceclip11-6358acb3b8cf3.png' width= '400'>
        <div></div>
        <a href='/home'>Go to previous page</a>
        <div></div>
        <a href='/space2'>Go to the next space picture</a>
        </html>
        ''')
@app.route('/space2')
def space2():
    return('''
        <html>
        <img src = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/81dde48b-5fdd-48c7-930d-a6670da31eb9/dfzba40-911ee1bf-303a-4d72-93c2-e7e9c67f1936.jpg/v1/fill/w_768,h_1024,q_75,strp/wolves_in_space__by_thenerdywonder_dfzba40-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAyNCIsInBhdGgiOiJcL2ZcLzgxZGRlNDhiLTVmZGQtNDhjNy05MzBkLWE2NjcwZGEzMWViOVwvZGZ6YmE0MC05MTFlZTFiZi0zMDNhLTRkNzItOTNjMi1lN2U5YzY3ZjE5MzYuanBnIiwid2lkdGgiOiI8PTc2OCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.yBdcjWGxgI4IxLgAnbw1T-YhdGjCEjS-p3k7EqZjvDk' width= '400'>
        <div></div>
        <a href='/space1'>Go to previous page</a>
        <div></div>
        <a href='/space3'>Go to the next space picture</a>
        </html>
        ''')
@app.route('/space3')
def space3():
    return('''
        <html>
        <img src = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/fd3a8fb7-5eef-4ae8-857d-977ef347f1e3/de2oy8m-d16160d2-a7f8-43d5-84fb-676f17dba08b.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2ZkM2E4ZmI3LTVlZWYtNGFlOC04NTdkLTk3N2VmMzQ3ZjFlM1wvZGUyb3k4bS1kMTYxNjBkMi1hN2Y4LTQzZDUtODRmYi02NzZmMTdkYmEwOGIuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.r-tJM6vqQt6bzloskpo1RNiBHPqmnMgb6U1sIQLJDuU' width= '400'>
        <div></div>
        <a href='/space2'>Go to the previous page</a>
        <div></div>
        <a href='/space1'>Go to the first space picture</a>
        </html>
        ''')

if __name__ == '__main__':
    app.run(debug=True)
