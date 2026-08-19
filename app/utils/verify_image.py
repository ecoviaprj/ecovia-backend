from gradio_client import Client, handle_file

def get_client():
    """Lazy load the Gradio client"""
    try:
        return Client("Kkkkiibii/trash-detect-tf")
    except Exception as e:
        print(f"Failed to initialize Gradio client: {e}")
        return None

def verify_image_with_gradio(image_path: str) -> bool:
    try:
        client = get_client()
        if client is None:
            print("Gradio client not available")
            return False
            
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
