def solution(video_len, pos, op_start, op_end, commands):
    
    # "mm:ss" → 초
    def to_seconds(time):
        minute = int(time[0:2])
        second = int(time[3:5])
        return minute * 60 + second
    
    # 초 → "mm:ss"
    def to_time(seconds):
        minute = seconds // 60
        second = seconds % 60
        return f"{minute:02d}:{second:02d}"
    
    # 모든 시간을 초 단위로 변환
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)
    
    for command in commands:
        
        # 현재 위치가 오프닝 구간이면 오프닝 끝으로 이동
        if op_start <= pos <= op_end:
            pos = op_end
        
        # 10초 전
        if command == "prev":
            pos = max(0, pos - 10)
        
        # 10초 후
        elif command == "next":
            pos = min(video_len, pos + 10)
        
        # 이동한 위치가 오프닝 구간이면 다시 오프닝 끝으로 이동
        if op_start <= pos <= op_end:
            pos = op_end
    
    return to_time(pos)