import arcade

arcade.open_window(600, 400, "Titulo")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
arcade.draw_text("Bem-vindo!", 250, 180, arcade.color.WHITE, 20)
arcade.finish_render()

arcade.run()
