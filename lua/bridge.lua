local input_file = "input.txt"
local frame_file = "frame.png"

while true do

    -- default no input
    local action = "NONE"

    local file = io.open(input_file, "r")
    if file then
        action = file:read("*l")  -- IMPORTANT: read line only
        file:close()
    end

    -- reset inputs every frame
    local buttons = {
        A=false, B=false,
        Up=false, Down=false,
        Left=false, Right=false
    }

    if action == "A" then buttons.A = true
    elseif action == "B" then buttons.B = true
    elseif action == "UP" then buttons.Up = true
    elseif action == "DOWN" then buttons.Down = true
    elseif action == "LEFT" then buttons.Left = true
    elseif action == "RIGHT" then buttons.Right = true
    end

    joypad.set(buttons)

    -- IMPORTANT: advance frame AFTER input set
    emu.frameadvance()

    -- screenshot AFTER frame update
    client.screenshot(frame_file)
end