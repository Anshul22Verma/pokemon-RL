local input_file = "input.txt"
local output_file = "frame.raw"

while true do

    -- Read action from Python
    local file = io.open(input_file, "r")
    local action = "NONE"

    if file then
        action = file:read("*all")
        file:close()
    end

    action = string.gsub(action, "%s+", "")

    -- Reset inputs
    joypad.set({
        A=false, B=false,
        Up=false, Down=false,
        Left=false, Right=false
    })

    -- Apply action
    if action == "A" then joypad.set({A=true})
    elseif action == "B" then joypad.set({B=true})
    elseif action == "UP" then joypad.set({Up=true})
    elseif action == "DOWN" then joypad.set({Down=true})
    elseif action == "LEFT" then joypad.set({Left=true})
    elseif action == "RIGHT" then joypad.set({Right=true})
    end

    -- Advance frame
    emu.frameadvance()

    -- Save screenshot every frame
    local img = gui.gdscreenshot()

    local f = io.open(output_file, "wb")
    f:write(img)
    f:close()
end