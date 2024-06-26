set -a
source .env
set +a

flask run &
flask_run_pid=$!

cleanup() {
  kill -9 $flask_run_pid
}

trap cleanup ERR SIGINT SIGTERM

pytest tests/

cleanup