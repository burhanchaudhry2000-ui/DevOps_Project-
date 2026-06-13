import tensorflow as tf
import sys

def inspect_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    print("--- INPUT DETAILS ---")
    for i, detail in enumerate(input_details):
        print(f"Input {i}: name={detail['name']}, shape={detail['shape']}, dtype={detail['dtype']}")
        
    print("\n--- OUTPUT DETAILS ---")
    for i, detail in enumerate(output_details):
        print(f"Output {i}: name={detail['name']}, shape={detail['shape']}, dtype={detail['dtype']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        inspect_model(sys.argv[1])
    else:
        print("Provide model path")
