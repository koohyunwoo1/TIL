import { useNavigate } from "react-router-dom";
import Modal from "../components/Common/Modal";
import Button from "../components/Common/Button";
import "../style/GameDescription.css";

const GameDescriptionModal = ({ isOpen, onClose, selectedGame }) => {
  const navigate = useNavigate();

  const navigateToGame = () => {
    navigate(`/${selectedGame}`);
    onClose();
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <div className="GameDescriptionContainer">
        <h1>게임 설명</h1>
        <p>
          {selectedGame === "drum" && (
            <>
              <span className="span-spacing">
                리듬 킹은 실제 드럼 소리를 바탕으로,
              </span>
              <span className="span-spacing">
                주어진 리듬 예시에 맞춰 드럼을 치는 게임입니다.
              </span>
              <span className="span-spacing">
                플레이어는 다양한 난이도의 리듬 패턴을 따라 치며,
              </span>
              <span className="span-spacing">
                음악적 감각을 기르고 스트레스를 해소할 수 있습니다.
              </span>
            </>
          )}
          {selectedGame === "piano" && (
            <>
              <span className="span-spacing">
                코드 천재는 실제 음 소리와 화음 소리를 바탕으로
              </span>
              <span className="span-spacing">구성된 흥미로운 게임입니다.</span>
              <span className="span-spacing">
                이 게임은 플레이어가 주어진 문제에 맞추어
              </span>
              <span className="span-spacing">정확한 음을 찾아야 하며,</span>
              <span className="span-spacing">
                이를 통해 음악에 대한 이해도를 높이고
              </span>
              <span className="span-spacing">
                감각을 기를 수 있도록 설계되었습니다.
              </span>
              <span className="span-spacing">
                음악적 재능을 발견하고 절대음감을 얻어보는 특별한 경험을 하게 될
                것입니다.
              </span>
            </>
          )}
          {selectedGame === "melody" && (
            <>
              <span className="span-spacing">
                퍼펙트 스코어는 노래에 대해 정확한 음을 발음하여
              </span>
              <span className="span-spacing">
                플레이어가 정해진 목표에 도달할 수 있도록 돕는
              </span>
              <span className="span-spacing">흥미로운 게임입니다.</span>
              <span className="span-spacing">
                이 게임은 각 음을 정확하게 찾아내는 데
              </span>
              <span className="span-spacing">중점을 두고 있으며,</span>
              <span className="span-spacing">
                자신의 음성과 음악적 감각을 발전시킬 수 있는 기회를 제공합니다.
              </span>
              <span className="span-spacing">
                다양한 레벨과 난이도를 통해 도전할 수 있으며,
              </span>
              <span className="span-spacing">
                음악적 재능을 더욱 빛낼 수 있는 경험을 하게 될 것입니다.
              </span>
            </>
          )}
        </p>

        <div className="GameDescriptionButton">
          <Button onClick={navigateToGame}>게임 하러 가기</Button>
        </div>
      </div>
    </Modal>
  );
};

export default GameDescriptionModal;
