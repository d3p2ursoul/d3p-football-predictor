"""Main entry point for the Football Predictor API"""
import os
from app import create_app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'production') == 'development'
    
    print(f"🚀 Football Predictor API starting on port {port}")
    print(f"📍 Environment: {'Development' if debug else 'Production'}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)