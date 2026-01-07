# 🎲 Splendor Elo Rating System

A web-based application for tracking and calculating Elo ratings for the board game Splendor using the OpenSkill library with the Plackett-Luce model.

## Features

- **OpenSkill Rating System**: Uses the Plackett-Luce model for accurate multi-player rankings.
- **Tournament Regions**: Register players to specific regions (e.g., North America, Europe, Asia).
- **Regional & Global Leaderboards**: Public page displaying current player rankings globally or filtered by region.
- **Ties Support**: Correctly handles tied outcomes in game results.
- **Player Management**: Admin can add players and assign them to regions.
- **Game Tracking**: Submit game results with placements (1st-4th) and points (1-15).
- **Player Statistics**: Detailed stats including win rate, average points, and placement distribution.
- **Game History**: View recent games and rating changes.
- **Admin Panel**: Secure admin interface for managing players, regions, and submitting results.
- **Responsive Design**: Modern, premium UI that works on desktop and mobile.

## Technology Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Rating System**: OpenSkill (Plackett-Luce model v5.0.0)
- **Database**: PostgreSQL (production) / SQLite (development)
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Styling**: Custom CSS with dark mode and glassmorphism

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL (for production) or SQLite (for development)

### Setup

1. **Clone or download this repository**

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**:
   - Copy `.env.example` to `.env`
   - Update the values as needed:
     ```
     SECRET_KEY=your-secret-key-here
     ADMIN_USERNAME=admin
     ADMIN_PASSWORD=your-password-here
     DATABASE_URL=sqlite:///splendor_ratings.db  # or PostgreSQL URL
     ```

6. **Initialize the database**:
   ```bash
   python app.py
   ```
   The database will be created automatically on first run.

7. **Run the application**:
   ```bash
   python app.py
   ```

8. **Access the application**:
   - Leaderboard: http://localhost:5000
   - Admin Panel: http://localhost:5000/admin

## Usage

### Admin Panel

1. Navigate to `/admin`
2. Login with your admin credentials (default: `admin` / `splendor2024`)
3. Add players using the "Player Management" section
4. Submit game results using the "Submit Game Results" section

### Submitting Game Results

1. Select the number of players (2-4)
2. For each placement (1st, 2nd, 3rd, 4th):
   - Select the player
   - Enter their points (1-15)
3. Click "Submit Game"
4. Ratings will be automatically calculated and updated

### Viewing Leaderboard

1. Navigate to the home page (`/`)
2. View current player rankings
3. Click "View Stats" on any player to see detailed statistics

## Rating System

The application uses the **OpenSkill** library with the **Plackett-Luce** model:

- **Initial Rating**: μ (mu) = 1000.0, σ (sigma) = 333.33
- **Displayed Rating**: μ (mu) rounded to the nearest whole number.
- **Rating Updates**: Calculated based on placement in each game, supporting ties.
- **Uncertainty**: Decreases as players play more games.

## Database Schema

### Region
- `id`: Primary key
- `name`: Region name (unique)

### Player
- `id`: Primary key
- `name`: Player name (unique)
- `region_id`: Foreign key to Region
- `mu`: Rating mean
- `sigma`: Rating uncertainty
- `games_played`: Total games
- `first_place`, `second_place`, `third_place`, `fourth_place`: Placement counts
- `total_points`: Cumulative points

### Game
- `id`: Primary key
- `played_at`: Timestamp
- `num_players`: Number of players (2-4)

### GameParticipant
- `id`: Primary key
- `game_id`: Foreign key to Game
- `player_id`: Foreign key to Player
- `placement`: Placement (1-4, allows same value for ties)
- `points`: Points scored (1-15)
- `mu_before`, `sigma_before`: Global rating before game
- `mu_after`, `sigma_after`: Global rating after game

## API Endpoints

### Public Endpoints

- `GET /api/leaderboard` - Get current rankings
- `GET /api/players` - Get all players
- `GET /api/players/<id>` - Get player details
- `GET /api/games` - Get game history

### Admin Endpoints (Authentication Required)

- `POST /api/admin/login` - Admin login
- `POST /api/admin/logout` - Admin logout
- `GET /api/admin/check` - Check login status
- `POST /api/admin/players` - Add new player
- `DELETE /api/admin/players/<id>` - Delete player
- `POST /api/admin/games` - Submit game results

## Deployment

### Local Development

Use SQLite for local development (default configuration).

### Production Deployment

#### Heroku

1. Create a Heroku app
2. Add PostgreSQL addon:
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```
3. Set environment variables:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set ADMIN_USERNAME=admin
   heroku config:set ADMIN_PASSWORD=your-password
   ```
4. Deploy:
   ```bash
   git push heroku main
   ```

#### Railway / Render

1. Create a new project
2. Add PostgreSQL database
3. Set environment variables
4. Deploy from GitHub or local repository

## Security Notes

- Change the default admin password in production
- Use a strong `SECRET_KEY` in production
- Consider implementing more robust authentication (OAuth, JWT) for production use
- Use HTTPS in production
- Regularly backup your database

## License

This project is open source and available for personal and commercial use.

## Support

For issues or questions, please create an issue in the repository.

## Credits

- **OpenSkill**: Rating system library
- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
