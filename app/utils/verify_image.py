from gradio_client import Client, handle_file

client = Client("Kkkkiibii/trash-detect-tf")

def verify_image_with_gradio(image_path: str) -> bool:
    try:
        result = client.predict(
            input_image=handle_file(image_path),
            api_name="/predict"
        )
        print("DEBUG Gradio result:", result)

        if isinstance(result, str):
            if "no trash" in result.lower():
                return True
            else:
                return False
        
        return False
    except Exception as e:
        print("Gradio verification failed:", e)
        return False
