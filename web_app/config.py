# MySQL database configuration
from sqlalchemy import create_engine
from web_app.app import app


USERNAME = 'lexi_vault'
PASSWORD = 'lexipass'
HOSTNAME = 'localhost'  # or your MySQL server's IP address
PORT = '3306'  # or your MySQL server's port
DATABASE_NAME = 'lexi_vault_db'

# Construct the MySQL connection URL
url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE_NAME}"

# Create the SQLAlchemy engine
engine = create_engine(url)
# Flask configuration

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
