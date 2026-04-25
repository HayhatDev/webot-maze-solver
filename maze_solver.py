from controller import Robot

robot = Robot()
time_step = 64

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_sensor = robot.getDevice("ps1")   # يسار (يكتشف الجدار)
front_sensor = robot.getDevice("ps7")  # أمامي

left_sensor.enable(time_step)
front_sensor.enable(time_step)

speed = 2.0
wall_detected = 100  # إذا تجاوز هذا الرقم، هناك جدار قريب

while robot.step(time_step) != -1:
    left = left_sensor.getValue()
    front = front_sensor.getValue()
    
    print(f"Left: {left:.0f}, Front: {front:.0f}")
    
    if front > wall_detected:
        # جدار أمامي -> لف يمين (لأنه لا يستطيع التقدم)
        print("جدار أمامي -> لف يمين")
        left_motor.setVelocity(-speed)
        right_motor.setVelocity(speed)
        robot.step(time_step * 15)
    elif left < wall_detected:
        # لا جدار على اليسار -> لف يسار (للبحث عن الجدار)
        print("لا جدار يسار -> لف يسار")
        left_motor.setVelocity(speed)
        right_motor.setVelocity(-speed)
        
    else:
        # جدار على اليسار -> تقدم للأمام
        print("جدار يسار -> تقدم")
        left_motor.setVelocity(speed)
        right_motor.setVelocity(speed)